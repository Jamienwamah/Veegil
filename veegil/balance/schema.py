import graphene
from graphene import List, Field, Decimal, ID, InputObjectType
from graphql.utilities import print_schema
from graphene_django.types import DjangoObjectType
from .models import Account

class AccountType(DjangoObjectType):
    class Meta:
        model = Account

class Query(graphene.ObjectType):
    accounts = List(AccountType)

    def resolve_accounts(self, info):
        return Account.objects.all()

class AccountInput(InputObjectType):
    user_id = ID(required=True)
    balance = Decimal()

class CreateAccount(graphene.Mutation):
    account = Field(AccountType)

    class Arguments:
        account_data = AccountInput(required=True)

    def mutate(self, info, account_data=None):
        user_id = account_data.pop('user_id')
        account = Account.objects.create(user_id=user_id, **account_data)
        return CreateAccount(account=account)

class UpdateAccount(graphene.Mutation):
    account = Field(AccountType)

    class Arguments:
        id = ID(required=True)
        account_data = AccountInput(required=True)

    def mutate(self, info, id, account_data=None):
        account = Account.objects.get(pk=id)
        if account_data.get('balance') is not None:
            account.balance = account_data['balance']
        account.save()
        return UpdateAccount(account=account)

class Mutation(graphene.ObjectType):
    create_account = CreateAccount.Field()
    update_account = UpdateAccount.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](http://127.0.0.1:8000/static/balance_schema.md)
"""
