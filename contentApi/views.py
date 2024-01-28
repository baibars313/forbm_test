from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Content
from .serializers import ContentSerializer 
# from .serializers import ContentSerializer
from django.db.models import Q
from rest_framework import serializers
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_media(request):
    user=request.user 
    if user is  None:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
        
    user_media = Content.objects.filter(user=user)
    common_media = Content.objects.filter(
        Q(content_type=Content.PUBLIC) | (Q(content_type=Content.GROUP) & Q(groups__in=user.contentgroup_set.all()))
    )
    accessible_media = user_media.union(common_media)
    serializer = ContentSerializer(accessible_media, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    



# Im storing media directly because ftp was a trouble for linux I updated it a few days ago 
# for better scurity we can create a seprate model oneToOne  realtion with content that will store refrence link of cloud storge or 
# file stoarge of every content instance and then we can serve it via a function that will check users authenticitiy 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_content(request):
    if 'src' not in request.FILES:
        return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data
    data['user'] = request.user.id

    serializer = ContentSerializer(data=data,context={'request': request})

    try:
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except serializers.ValidationError as e:
        return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
