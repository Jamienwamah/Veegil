from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework_api_key.permissions import HasAPIKey
from datetime import timedelta
import datetime
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User
from .serializers import UserSerializer
from . import serializers
from otp.models import OTP
import uuid


class CustomUserAPIView(GenericAPIView):
    permission_classes  = [AllowAny,]
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Create a new user with the given username, email, and password.",
        responses={200: openapi.Response('User created successfully')}
    )

    # def get(self, request, *args, **kwargs):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new user with the given username, email, and password.

        ---
        parameters:
          - name: username
            in: query
            description: The username of the user.
            required: true
            type: string
          - name: email
            in: query
            description: The email of the user.
            required: true
            type: string
          - name: password
            in: query
            description: The password of the user.
            required: true
            type: string
        """
        user_data=request.data
        serializer = self.serializer_class(data=user_data)
        try:
          if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            print(user_data)
            #It sends otp to users mail
            return Response ({
              'data': user_data,
              'message': f'hi {user_data["first_name"]}, congratulations!!!. An otp has been sent to your mail, kindly verify your account to complete your registeration'
            }, status= status.HTTP_201_CREATED)
        except IntegrityError as e:
                if 'username' in str(e):
                    return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
                elif 'email' in str(e):
                    return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
                elif 'password' in str(e):  
                    return Response({'error': 'Password error.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': "Account created successfully! An OTP to confirm your verification has been sent to your mail"},
                                    status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)