from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer
import random
from datetime import datetime, timedelta

class CustomUserAPIView(APIView):
    permission_classes = (AllowAny,) 
    
    def get(self, request, *args, **kwargs):
        return Response({'error': 'GET method is not allowed for this endpoint.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            date_of_birth_str = serializer.validated_data.get('date_of_birth')
            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
            today = datetime.today().date()
            age_limit_date = date_of_birth + timedelta(days=365 * 18)

            if today < age_limit_date:
                return Response({"error": "Users must be at least 18 years old to register."},
                                status=status.HTTP_400_BAD_REQUEST)

            username = serializer.validated_data.get('username')
            if len(username) < 7:
                return Response({"error": "Username must be at least 7 characters long."},
                                status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(username=username).exists():
                return Response({"error": {"username": ["Username already exists."]}},
                                status=status.HTTP_400_BAD_REQUEST)
                
            # Generate account number
            account_number = self.generate_account_number()
            serializer.validated_data['account_number'] = account_number

            try:
                user = serializer.save()

               
                token, _ = Token.objects.get_or_create(user=user)

                return Response({'message': 'Registration was successful'}, status=status.HTTP_200_OK)

            except IntegrityError as e:
                if 'username' in str(e):
                    return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
                elif 'email' in str(e):
                    return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
                elif 'password' in str(e):
                    return Response({'error': 'Password error.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': "An OTP to complete your account verification has been sent to your mail"},
                                    status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])
