from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from signup.models import User
from .models import Transfer
from .serializers import TransferSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerOrReadOnly  # Assuming you have a custom permission class

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])  
def transfer_money(request):
    sender = request.user 
    receiver_account_number = request.data.get('receiver_account_number')
    amount = request.data.get('amount')

    try:
        receiver = User.objects.get(profile__account_number=receiver_account_number)
    except User.DoesNotExist:
        return Response({'error': 'Receiver user not found'}, status=status.HTTP_404_NOT_FOUND)

    if sender == receiver:
        return Response({'error': 'Cannot transfer money to yourself'}, status=status.HTTP_400_BAD_REQUEST)

    sender_balance = sender.profile.balance if hasattr(sender, 'profile') else 0
    if sender_balance < amount:
        return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

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
