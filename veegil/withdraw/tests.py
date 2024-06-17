from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Withdraw
from signup.models import User

class WithdrawAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.account_number = '1234567890'  
        self.user.profile.account_number = self.account_number
        self.user.profile.balance = 1000  
        self.user.save()

    def test_valid_withdrawal(self):
        url = reverse('withdraw')
        data = {'account_number': self.account_number, 'amount': 500}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Withdraw.objects.count(), 1)
        self.assertEqual(self.user.profile.balance, 500)  

    def test_invalid_account_number(self):
        url = reverse('withdraw')
        data = {'account_number': 'invalid_account_number', 'amount': 500}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_insufficient_balance(self):
        url = reverse('withdraw')
        data = {'account_number': self.account_number, 'amount': 1500} 
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
