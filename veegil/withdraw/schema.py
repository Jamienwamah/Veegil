import graphene
from graphene import List
from graphene_django.types import DjangoObjectType
from .models import Withdraw

class WithdrawType(DjangoObjectType):
    class Meta:
        model = Withdraw

class Query(graphene.ObjectType):
    withdraws = List(WithdrawType)

    def resolve_withdraws(self, info):  # Corrected method name
        return Withdraw.objects.all()

schema = graphene.Schema(query=Query)
