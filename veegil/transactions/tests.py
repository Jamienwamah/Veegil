from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Transaction
from signup.models import User

class TransactionHistoryAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.sender = User.objects.create_user(username='sender', email='sender@example.com', password='password')
        self.receiver = User.objects.create_user(username='receiver', email='receiver@example.com', password='password')
        self.transaction1 = Transaction.objects.create(sender=self.sender, receiver=self.user, amount=100)
        self.transaction2 = Transaction.objects.create(sender=self.user, receiver=self.receiver, amount=200)

    def test_get_transaction_history(self):
        url = reverse('transaction_history')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if all transactions are returned
        self.assertEqual(response.data[0]['sender'], self.sender.id)  # Check if the first transaction sender is correct
        self.assertEqual(response.data[0]['receiver'], self.user.id)  # Check if the first transaction receiver is correct
        self.assertEqual(response.data[0]['amount'], 100)  # Check if the first transaction amount is correct
        self.assertEqual(response.data[1]['sender'], self.user.id)  # Check if the second transaction sender is correct
        self.assertEqual(response.data[1]['receiver'], self.receiver.id)  # Check if the second transaction receiver is correct
        self.assertEqual(response.data[1]['amount'], 200)  # Check if the second transaction amount is correct
