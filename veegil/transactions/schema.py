import graphene
from graphene_django.types import ObjectType
from graphene import List
from .models import Transaction
from graphene_django.types import DjangoObjectType

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction

class Query(ObjectType):
    transactions = List(TransactionType)

    def resolve_transaction(self, info):
        return Transaction.objects.all()

schema = graphene.Schema(query=Query)
