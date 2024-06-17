from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.

class ProfileView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
