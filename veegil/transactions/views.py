from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

@api_view(['GET'])
def transaction_history(request):
    user = request.user  # Assuming user is authenticated
    sent_transactions = Transaction.objects.filter(sender=user)
    received_transactions = Transaction.objects.filter(receiver=user)
    transactions = sent_transactions | received_transactions
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)
