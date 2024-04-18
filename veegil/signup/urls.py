from django.urls import path
from .views import CustomUserAPIView


urlpatterns = [
    path('auth/register/', CustomUserAPIView.as_view(), name='register'),
]