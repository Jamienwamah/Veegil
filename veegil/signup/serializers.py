from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError 
from django.core.validators import MinLengthValidator
from datetime import datetime
from .models import User
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
    date_of_birth = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Enter your date of birth.',
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
    
    account_number = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        
    def validate_first_name(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('Please input your first name.')
        return value

    def validate_last_name(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('Please input your last name.')
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
    
    def validate_email(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('Email is needed.')
        return value
    
    def validate_date_of_birth(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise serializers.ValidationError('Date of birth must be in YYYY-MM-DD format.')
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")

        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")

        if not re.search(r'[#!%&$@*]', value):
            raise serializers.ValidationError("Password must contain at least one special character from (#!%&$@*).")

        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def validate_gender(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('Enter your gender.')
        return value
    
    def validate_residential_address(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('Enter residential address.')
        return value
    
    def create(self, validated_data):
        try:
            user = User.objects.create(**validated_data)
        except IntegrityError as e:
            if 'phone_number' in e.args[0]: 
                raise serializers.ValidationError({"error":{"phone_number":["Phone number must be unique."]}})
            elif 'username' in e.args[0]: 
                raise serializers.ValidationError({"error": {"username": ["Username already exists."]}})
            elif 'email' in e.args[0]:  
                raise serializers.ValidationError({"error": {"email": ["Email already exists."]}})
            else:
                raise serializers.ValidationError({"error":["An error occurred while creating the user."]})
        else:
            return {"Registration was successful"}

