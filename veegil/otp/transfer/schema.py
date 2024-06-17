import graphene
from graphene import List, Field, Decimal, ID
from graphene_django.types import DjangoObjectType
from graphql.utilities import print_schema
from .models import Transfer
from django.utils import timezone

class TransferType(DjangoObjectType):
    class Meta:
        model = Transfer

class Query(graphene.ObjectType):
    transfers = List(TransferType)

    def resolve_transfers(self, info):  
        return Transfer.objects.all()

class CreateTransfer(graphene.Mutation):
    transfer = graphene.Field(TransferType)

    class Arguments:
        sender_id = ID(required=True)
        receiver_id = ID(required=True)
        amount = Decimal(required=True)
        type = graphene.String(required=False)

    def mutate(self, info, sender_id, receiver_id, amount, type=None):
        transfer = Transfer.objects.create(
            sender_id=sender_id,
            receiver_id=receiver_id,
            amount=amount,
            type=type if type else 'transfer',
            timestamp=timezone.now()
        )
        return CreateTransfer(transfer=transfer)

class Mutation(graphene.ObjectType):
    create_transfer = CreateTransfer.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](http://127.0.0.1:8000/static/transfer_schema.md)
"""

