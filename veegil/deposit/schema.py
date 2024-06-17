import graphene
from graphene import List
from graphql.utilities import print_schema
from graphene_django.types import DjangoObjectType
from .models import Deposit

class DepositType(DjangoObjectType):
    class Meta:
        model = Deposit

class Query(graphene.ObjectType):
    deposits = List(DepositType)

    def resolve_deposits(self, info):
        return Deposit.objects.all()

class CreateDeposit(graphene.Mutation):
    deposit = graphene.Field(DepositType)

    class Arguments:
        user_id = graphene.Int(required=True)
        amount = graphene.Decimal(required=True)
        account_number = graphene.UUID()

    def mutate(self, info, user_id, amount, account_number=None):
        deposit = Deposit.objects.create(user_id=user_id, amount=amount, account_number=account_number)
        return CreateDeposit(deposit=deposit)

class Mutation(graphene.ObjectType):
    create_deposit = CreateDeposit.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](https://bankapp-hd3c.onrender.com/static/deposit_schema.md)
"""


