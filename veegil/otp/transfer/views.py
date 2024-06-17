from rest_framework.response import Response
from rest_framework import status
from signup.models import User
from .models import Transfer
from .serializers import TransferSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['POST'])
@permission_classes([AllowAny,])
@swagger_auto_schema(
    operation_description="Transfer money from the authenticated user's account to another user's account.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['receiver_account_number', 'amount'],
        properties={
            'receiver_account_number': openapi.Schema(type=openapi.TYPE_STRING, description="The account number of the receiver."),
            'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description="The amount to transfer.")
        }
    ),
    responses={
        201: TransferSerializer,
        400: "Bad request",
        404: "Receiver user not found",
        500: "Internal Server Error"
    }
)
def transfer_money(request):
    """
    Transfer money from the authenticated user's account to another user's account.

    ---
    parameters:
      - name: receiver_account_number
        in: query
        description: The account number of the receiver.
        required: true
        type: string
      - name: amount
        in: query
        description: The amount to transfer.
        required: true
        type: number
    """
    sender = request.user
    account_number = request.data.get('receiver_account_number')
    amount = request.data.get('amount')

    try:
        receiver = User.objects.get(phone_number=account_number)
    except User.DoesNotExist:
        return Response({'error': 'Receiver user not found'}, status=status.HTTP_404_NOT_FOUND)

    if sender == receiver:
        return Response({'error': 'Cannot transfer money to yourself'}, status=status.HTTP_400_BAD_REQUEST)

    sender_balance = sender.profile.balance if hasattr(sender, 'profile') else 0
    if sender_balance < amount:
        return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        with transaction.atomic():
            sender.profile.balance -= amount
            sender.profile.save()
            receiver.profile.balance += amount
            receiver.profile.save()

            transaction = Transfer.objects.create(
                sender=sender,
                receiver=receiver,
                amount=amount,
                type='transfer'
            )
            serializer = TransferSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
