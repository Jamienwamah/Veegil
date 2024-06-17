from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User
from django.db import IntegrityError
import re


class UserSerializer(serializers.ModelSerializer):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    first_name = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Please input your first name.',
    })
    last_name = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Please input your last name.',
    })
    username = serializers.CharField(write_only=True, required=True, min_length=7, error_messages={
        'required': 'Input username.',
        'min_length': 'Username must be at least 7 characters long.',
    })
    email = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Email is needed.',
    })
    phone_number = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Input phone number.',
    })
    password = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Input a password',
    })
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=True, error_messages={
        'required': 'Enter your gender.',
    })
    residential_address = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Enter residential address.',
    })
    password2 = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Input a password',
    })

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("Passwords do not match")
        hashed_password = make_password(password)
        attrs['password'] = hashed_password
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            phone_number=validated_data.get('phone_number'),
            password=validated_data.get('password'),
            password2=validated_data.get('password2'),
            gender=validated_data.get('gender'),
        )
        return super().create(validated_data)