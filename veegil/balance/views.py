from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.dispatch import receiver
from signup.models import User
from django.db.models.signals import post_save
from .models import Account
from .serializers import AccountSerializers
from withdraw.models import Withdraw
from deposit.models import Deposit
from transfer.models import Transfer

class BalanceAPIView(APIView):
    def get(self, request):
        account = Account.objects.get(user=request.user)
        return Response({'balance': account.balance})

    @staticmethod
    @receiver(post_save, sender=Withdraw)
    @receiver(post_save, sender=Deposit)
    @receiver(post_save, sender=Transfer)
    def update_balance(sender, instance, **kwargs):
        user = instance.user
        account, _ = Account.objects.get_or_create(user=user)
        if sender == Withdraw or sender == Transfer:
            account.balance -= instance.amount
        elif sender == Deposit:
            account.balance += instance.amount
        account.save()
