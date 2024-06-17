from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Transfer
from signup.models import User

class TransferAPITest(APITestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', email='sender@example.com', password='password')
        self.receiver = User.objects.create_user(username='receiver', email='receiver@example.com', password='password')
        self.sender.profile.balance = 1000  # Initial balance for sender
        self.receiver.profile.balance = 500  # Initial balance for receiver
        self.sender.profile.save()
        self.receiver.profile.save()

    def test_valid_transfer(self):
        url = reverse('transfer')
        data = {'receiver_account_number': self.receiver.profile.account_number, 'amount': 200}
        self.client.force_authenticate(user=self.sender)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transfer.objects.count(), 1)
        self.assertEqual(self.sender.profile.balance, 800)  # Check if sender balance has been updated
        self.assertEqual(self.receiver.profile.balance, 700)  # Check if receiver balance has been updated

    def test_receiver_not_found(self):
        url = reverse('transfer')
        data = {'receiver_account_number': 'invalid_account_number', 'amount': 200}
        self.client.force_authenticate(user=self.sender)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_insufficient_balance(self):
        url = reverse('transfer')
        data = {'receiver_account_number': self.receiver.profile.account_number, 'amount': 1500}  # Amount exceeds sender balance
        self.client.force_authenticate(user=self.sender)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transfer_to_self(self):
        url = reverse('transfer')
        data = {'receiver_account_number': self.sender.profile.account_number, 'amount': 200}  # Transfer to self
        self.client.force_authenticate(user=self.sender)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
