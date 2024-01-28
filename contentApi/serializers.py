from rest_framework import serializers
from .models import Content
from authApi.models import ContentGroup

class ContentSerializer(serializers.ModelSerializer):
    content_type = serializers.ChoiceField(choices=Content.ACCESS_CHOICES)
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=ContentGroup.objects.all())
    class Meta:
        model = Content
        fields = '__all__'  
    
    def validate_groups(self, value):
        user = self.context['request'].user
        print(user.id == value[0].creater.id)
        valid_groups = [group for group in value if user  in group.users.all() or user.id == group.creater.id ]
        if  not valid_groups:
            raise serializers.ValidationError("Invalid groups: You can only add groups associated with you.")
        return value
        
    