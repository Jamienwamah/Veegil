# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Withdraw
from signup.models import User
from .serializers import WithdrawSerializer

class Withdraw(APIView):
    def post(self, request):
        account_number = request.data.get('account_number')
        amount = request.data.get('amount')

        if not account_number or not amount:
            return Response({'error': 'Both account number and amount are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify account number
        user = self.verify_account_number(account_number)
        if not user:
            return Response({'error': 'Invalid account number'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user has sufficient balance
        if user.balance < amount:
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

        # Perform withdrawal
        user.balance -= amount
        user.save()

        withdrawal = Withdraw.objects.create(
            user=user,
            amount=amount
        )

        serializer = WithdrawSerializer(withdrawal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def verify_account_number(self, account_number):
        try:
            user = User.objects.get(account_number=account_number)
            return User
        except User.DoesNotExist:
            return None
