import graphene
from graphene import List, Field, Decimal, ID
from graphene_django.types import DjangoObjectType
from graphql.utilities import print_schema
from .models import Withdraw
from django.utils import timezone

class WithdrawType(DjangoObjectType):
    class Meta:
        model = Withdraw

class Query(graphene.ObjectType):
    withdraws = List(WithdrawType)

    def resolve_withdraws(self, info):  
        return Withdraw.objects.all()

class CreateWithdraw(graphene.Mutation):
    withdraw = graphene.Field(WithdrawType)

    class Arguments:
        user_id = ID(required=True)
        amount = Decimal(required=True)
        type = graphene.String(required=False) 

    def mutate(self, info, user_id, amount, type=None):
        withdraw = Withdraw.objects.create(
            user_id=user_id,
            amount=amount,
            type=type if type else 'withdraw',
            timestamp=timezone.now()
        )
        return CreateWithdraw(withdraw=withdraw)

class Mutation(graphene.ObjectType):
    create_withdraw = CreateWithdraw.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](http://127.0.0.1:8000/static/withdraw_schema.md)
"""
