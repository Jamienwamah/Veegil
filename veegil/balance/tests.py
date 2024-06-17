from django.test import TestCase
from signup.models import User
from rest_framework.test import APIClient
from .models import Account
from .serializers import AccountSerializer
from rest_framework import status

class BalanceAPIViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.account = Account.objects.create(user=self.user, balance=1000)
        self.client = APIClient()

    def test_get_balance(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/balance/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, AccountSerializer(self.account).data)

    def test_update_balance_on_withdraw(self):
        withdraw_amount = 100
        self.client.force_login(self.user)
        response = self.client.post('/api/withdraw/', {'amount': withdraw_amount}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        updated_account = Account.objects.get(user=self.user)
        self.assertEqual(updated_account.balance, self.account.balance - withdraw_amount)

    def test_update_balance_on_deposit(self):
        deposit_amount = 200
        self.client.force_login(self.user)
        response = self.client.post('/api/deposit/', {'amount': deposit_amount}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        updated_account = Account.objects.get(user=self.user)
        self.assertEqual(updated_account.balance, self.account.balance + deposit_amount)

    def test_update_balance_on_transfer(self):
        transfer_amount = 300
        recipient = User.objects.create_user(username='recipient', email='recipient@example.com', password='password')
        self.client.force_login(self.user)
        response = self.client.post('/api/transfer/', {'amount': transfer_amount, 'recipient': recipient.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        updated_account = Account.objects.get(user=self.user)
        self.assertEqual(updated_account.balance, self.account.balance - transfer_amount)
