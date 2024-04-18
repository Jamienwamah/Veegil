from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import AccessToken, RefreshToken
from .serializers import AccessTokenSerializer, RefreshTokenSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from signup.models import User
from django.contrib.auth import authenticate


#Create views here

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            
            AccessToken.objects.create(user=user, token=str(access))
            RefreshToken.objects.create(user=user, token=str(refresh))
            
            access_serializers = AccessTokenSerializers(access)
            refresh_serializers = RefreshTokenSerializer(refresh)
        
            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)