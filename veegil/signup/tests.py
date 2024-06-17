from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class CustomUserAPIViewTest(APITestCase):
    def test_create_user_successfully(self):
        url = 'auth/register'
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password', 'date_of_birth': '1990-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Registration was successful')

    def test_create_user_under_age(self):
        url = 'auth/register'
        data = {'username': 'underageuser', 'email': 'underage@example.com', 'password': 'password', 'date_of_birth': '2023-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Users must be at least 18 years old to register.')

    def test_create_user_short_username(self):
        url = 'auth/register'
        data = {'username': 'short', 'email': 'short@example.com', 'password': 'password', 'date_of_birth': '1990-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Username must be at least 7 characters long.')

    def test_create_user_existing_username(self):
        User.objects.create_user(username='existinguser', email='existing@example.com', password='password')
        url = 'auth/register'
        data = {'username': 'existinguser', 'email': 'new@example.com', 'password': 'password', 'date_of_birth': '1990-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error']['username'][0], 'Username already exists.')

    def test_create_user_existing_email(self):
        User.objects.create_user(username='newuser', email='existing@example.com', password='password')
        url = 'auth/register'
        data = {'username': 'newuser', 'email': 'existing@example.com', 'password': 'password', 'date_of_birth': '1990-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Email already exists.')
