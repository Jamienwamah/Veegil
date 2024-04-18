import graphene
from graphene import List
from graphene_django.types import DjangoObjectType
from .models import Deposit

class DepositType(DjangoObjectType):
    class Meta:
        model = Deposit

class Query(graphene.ObjectType):
    deposits = List(DepositType)

    def resolve_deposits(self, info):
        return Deposit.objects.all()

schema = graphene.Schema(query=Query)
