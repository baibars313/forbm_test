from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ContentGroup
from .serializers import ContentGroupSerializer  # You need to create a serializer for your model
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def content_group_list(request):
    if request.method == 'GET':
        content_groups = ContentGroup.objects.filter(creater=request.user)
        serializer = ContentGroupSerializer(content_groups, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        users = request.data.get('users', [])
        serializer = ContentGroupSerializer(data=request.data)
        try:
            if serializer.is_valid():
                content_group = serializer.save(creater=request.user)
                content_group.users.set(users)
                content_group.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise ValidationError(serializer.errors)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_users_to_group(request, group_id):
    try:
        content_group = ContentGroup.objects.get(pk=group_id, creater=request.user)
    except ContentGroup.DoesNotExist:
        return Response({'error': 'ContentGroup does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        try:
            user_ids = request.data.get('user_ids', [])
            content_group.users.add(*user_ids)
            content_group.save()
            serializer = ContentGroupSerializer(content_group)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)