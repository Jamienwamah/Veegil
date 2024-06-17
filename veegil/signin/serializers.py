from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from signup.models import User


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=120, required=True, min_length=3)
    password = serializers.CharField(max_length=100, required=True, style={'input_type': 'password'}, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'access_token', 'refresh_token']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Retrieve user based on email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": "User with this email does not exist"}, code=status.HTTP_404_NOT_FOUND)

        # Validate password
        if not user.check_password(password):
            raise serializers.ValidationError({"error": "Invalid password"}, code=status.HTTP_401_UNAUTHORIZED)

        # Generate tokens
        try:
            token = RefreshToken.for_user(user)
        except TokenError as e:
            raise serializers.ValidationError({"error": "Token generation failed"}, code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return {
            'id': user.id,
            'email': user.email,
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        }
