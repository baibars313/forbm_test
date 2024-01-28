# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ContentGroup

from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')  # Add any additional fields you need


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',"id"]

class ContentGroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)  # Represent user names in 'users' field
    creater = UserSerializer(read_only=True)  # Represent the creater's username
    # Customize representation of the 'description' field if needed

    class Meta:
        model = ContentGroup
        fields = ['id', 'users', 'creater', 'group_name', 'description']
        