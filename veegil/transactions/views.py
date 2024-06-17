from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TransactionHistory 
from withdraw.models import Withdraw
from deposit.models import Deposit
from transfer.models import Transfer
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(
    operation_description="Get transaction history for the authenticated user.",
    responses={200: TransactionSerializer(many=True)}
)
def transaction_history(request):
    """
    Get transaction history for the authenticated user.

    Returns a list of all transactions (sent and received) for the authenticated user.

    ---
    responses:
      200:
        description: A list of all transactions for the authenticated user.
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Transaction'
    """
    try:
        user_id = request.user.id
        sent_withdrawals = Withdraw.objects.filter(sender=user_id)
        sent_deposits = Deposit.objects.filter(sender=user_id)
        sent_transfers = Transfer.objects.filter(sender=user_id)

        received_withdrawals = Withdraw.objects.filter(receiver=user_id)
        received_deposits = Deposit.objects.filter(receiver=user_id)
        received_transfers = Transfer.objects.filter(receiver=user_id)

        sent_transactions = list(sent_withdrawals) + list(sent_deposits) + list(sent_transfers)
        received_transactions = list(received_withdrawals) + list(received_deposits) + list(received_transfers)

        transactions = sent_transactions + received_transactions

        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "User not found."}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
