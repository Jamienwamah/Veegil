import graphene
from graphene_django.types import ObjectType
from graphene import List, Field, String, Decimal
from graphql.utilities import print_schema
from .models import TransactionHistory
from graphene_django.types import DjangoObjectType
from django.utils import timezone

class TransactionType(DjangoObjectType):
    class Meta:
        model = TransactionHistory

class Query(ObjectType):
    transactions = List(TransactionType)

    def resolve_transactions(self, info):
        return TransactionHistory.objects.all()

class CreateTransaction(graphene.Mutation):
    transaction = graphene.Field(TransactionType)

    class Arguments:
        sender_id = graphene.ID(required=True)
        receiver_id = graphene.ID(required=True)
        amount = Decimal(required=True)
        type = String(required=True)

    def mutate(self, info, sender_id, receiver_id, amount, type):
        transaction = TransactionHistory.objects.create(
            sender_id=sender_id,
            receiver_id=receiver_id,
            amount=amount,
            type=type,
            timestamp=timezone.now()
        )
        return CreateTransaction(transaction=transaction)

class Mutation(ObjectType):
    create_transaction = CreateTransaction.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](http://127.0.0.1:8000/static/transactions_schema.md)
"""

