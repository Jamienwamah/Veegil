from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from decimal import Decimal
from signup.models import User
from .models import Deposit
from signup.serializers import UserSerializer
from .serializers import DepositSerializer
from drf_yasg.utils import swagger_auto_schema

class DepositAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="This endpoint allows users to make deposits."
    )
    def post(self, request):
        """
        Endpoint to deposit money to a user's account.

        ---
        parameters:
          - name: phone_number
            in: query
            description: The phone number of the user to deposit money to.
            required: true
            type: string
          - name: amount
            in: query
            description: The amount of money to deposit.
            required: true
            type: number
        """
        phone_number = request.data.get('phone_number')
        amount = request.data.get('amount')

        if not phone_number or not amount:
            return Response({'message': 'Phone number and amount are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return Response({'error': 'User with this phone number does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Update user balance
        user.balance += Decimal(amount)
        user.save()

        # Create deposit transaction
        transaction = Deposit.objects.create(
            user=user,
            amount=float(amount),
            type='deposit'
        )
        serializer = DepositSerializer(transaction)
        user_serializer = UserSerializer(user)

        response_data = {
            'transaction': serializer.data,
            'user': user_serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
