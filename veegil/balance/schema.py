import graphene
from graphene import List
from graphene_django.types import DjangoObjectType
from .models import Account

class AccountType(DjangoObjectType):
    class Meta:
        model = Account

class Query(graphene.ObjectType):
    accounts = List(AccountType)

    def resolve_accounts(self, info):  # Corrected method name
        return Account.objects.all()

schema = graphene.Schema(query=Query)
