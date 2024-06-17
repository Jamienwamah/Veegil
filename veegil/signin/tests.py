from signup.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import AccessToken, RefreshToken
from .serializers import LoginSerializer, LogoutSerializer

class LoginAPIViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client = APIClient()

    def test_login_success(self):
        url = '/api/login/'
        data = {'username': 'testuser', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class LogoutAPIViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.access_token = AccessToken.objects.create(user=self.user)
        self.refresh_token = RefreshToken.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))

    def test_logout_success(self):
        url = '/api/logout/'
        data = {'refresh': str(self.refresh_token)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
