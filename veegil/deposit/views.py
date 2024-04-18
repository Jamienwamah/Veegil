from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from signup.models import User 
from .models import Deposit
from signup.serializers import UserSerializer
from .serializers import DepositSerializer

class Deposit(APIView):
    def post(self, request):
        account_number = request.data.get('account_number')
        amount = request.data.get('amount')

        if not account_number or not amount:
            return Response({'error': 'Both account number and amount are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(account_number=account_number)
        except User.DoesNotExist:
            return Response({'error': 'User with this account number does not exist'}, status=status.HTTP_404_NOT_FOUND)

        user.balance += amount
        user.save()

        transaction = Deposit.objects.create(
            user=user,
            amount=amount,
            type='deposit'
        )
        serializer = DepositSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
