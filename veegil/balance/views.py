from rest_framework.views import APIView
from rest_framework.response import Response
from django.dispatch import receiver
from signup.models import User
from django.db.models.signals import post_save
from .models import Account
from .serializers import AccountSerializer
from withdraw.models import Withdraw
from deposit.models import Deposit
from transfer.models import Transfer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from decimal import Decimal

class BalanceAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve the balance of the current user's account."
    )
    def get(self, request):
        """
        Retrieve the balance of the current user's account.
        """
        user = request.user
        account, _ = Account.objects.get_or_create(user=user)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

@receiver(post_save, sender=Withdraw)
@receiver(post_save, sender=Deposit)
@receiver(post_save, sender=Transfer)
def update_balance(sender, instance, created, **kwargs):
    user = instance.user
    account, _ = Account.objects.get_or_create(user=user)

    if sender == Withdraw:
        account.balance -= instance.amount
    elif sender == Deposit:
        # Convert instance.amount to Decimal before adding
        amount = Decimal(instance.amount)
        
        # Convert the balance to Decimal if it's not already
        balance = Decimal(account.balance)
        
        # Perform the addition operation
        new_balance = balance + amount
        
        # Update the account balance
        account.balance = new_balance
    elif sender == Transfer:
        account.balance -= instance.amount

    account.save()
