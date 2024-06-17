from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from balance.models import Account
from rest_framework import status
from .models import Withdraw
from signup.models import User
from .serializers import WithdrawSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class Withdraw(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_classes = [IsAuthenticated,] 
        
    @swagger_auto_schema(
        operation_description="Allows authenticated users to make withdrawals from their account.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['account_number', 'amount'],
            properties={
                'account_number': openapi.Schema(type=openapi.TYPE_STRING, description="The account number to withdraw from."),
                'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description="The amount to withdraw.")
            }
        ),
        responses={
            201: WithdrawSerializer,
            400: "Bad request",
            401: "Unauthorized",
            404: "Invalid account number",
            500: "Internal Server Error"
        }
    )
    def post(self, request):
        """
        Allows authenticated users to make withdrawals from their account.

        ---
        parameters:
          - name: account_number
            in: query
            description: The account number to withdraw from.
            required: true
            type: string
          - name: amount
            in: query
            description: The amount to withdraw.
            required: true
            type: number
        """
        account_number = request.data.get('account_number')
        amount = request.data.get('amount')
        if not account_number or not amount:
            return Response({'error': 'Both account number and amount are required'}, status=status.HTTP_400_BAD_REQUEST)

     # Verify account number and retrieve related Balance object
        user, balance = self.verify_account_number(account_number)
        if not user or not balance:
            return Response({'error': 'Invalid account number'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Withdrawal was successful'}, status=status.HTTP_200_OK)


        # Check if the user's balance has sufficient balance
        if balance.amount < amount:
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Withdrawal was successful'}, status=status.HTTP_200_OK)

        # Perform withdrawal
        try:
            with transaction.atomic():
                balance.amount -= amount
                balance.save()

                withdrawal = Withdraw.objects.create(
                    user=user,
                    phone_number=account_number,
                    amount=amount,
                    type=type,
                )
        except IntegrityError as e:
            return Response({'error': 'An error occurred while processing the withdrawal'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = WithdrawSerializer(withdrawal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def verify_account_number(self, account_number):
        """
        Allows authenticated users to verify their accounts before they can make withdrawals.

        ---
        parameters:
        -name: account_number
            in: query
            description: The account number to withdraw from.
            required: true
            type: string
        - name: amount
            in: query
            description: The amount to withdraw.
            required: true
            type: number
        """
        try:
            user = User.objects.get(phone_number=account_number)
            balance = Account.objects.get(user=user)  
            return user, balance
        except User.DoesNotExist:
            return None, None
        except Account.DoesNotExist:
            return None, None