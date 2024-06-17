from signup.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Deposit
from signup.serializers import UserSerializer
from .serializers import DepositSerializer

class DepositAPIViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_deposit_success(self):
        url = '/api/deposit/'
        data = {'phone_number': '1234567890', 'amount': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the user balance is updated correctly
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.balance, 100)

        # Check if the deposit transaction is created correctly
        deposit_transaction = Deposit.objects.get(user=self.user)
        self.assertEqual(deposit_transaction.amount, 100)

        # Check if the response contains the expected data
        expected_response_data = {
            'transaction': DepositSerializer(deposit_transaction).data,
            'user': UserSerializer(updated_user).data
        }
        self.assertEqual(response.data, expected_response_data)

    def test_deposit_missing_fields(self):
        url = '/api/deposit/'
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
