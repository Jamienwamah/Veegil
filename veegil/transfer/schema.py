import graphene
from graphene import List
from graphene_django.types import DjangoObjectType
from .models import Transfer

class TransferType(DjangoObjectType):
    class Meta:
        model = Transfer

class Query(graphene.ObjectType):
    transfers = List(TransferType)

    def resolve_transfers(self, info):  # Corrected method name
        return Transfer.objects.all()

schema = graphene.Schema(query=Query)
