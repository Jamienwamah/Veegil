import graphene
from graphene import List, ObjectType
from graphene_django.types import DjangoObjectType
from graphql.utilities import print_schema
from .models import AccessToken, RefreshToken

class UserType(DjangoObjectType):
    class Meta:
        model = AccessToken

class RefreshTokenType(DjangoObjectType):
    class Meta:
        model = RefreshToken

class Query(ObjectType):
    access_tokens = List(UserType)
    refresh_tokens = List(RefreshTokenType)

    def resolve_access_tokens(self, info):
        return AccessToken.objects.all()

    def resolve_refresh_tokens(self, info):
        return RefreshToken.objects.all()

class CreateAccessToken(graphene.Mutation):
    access_token = graphene.Field(UserType)

    class Arguments:
        user_id = graphene.Int(required=True)
        token = graphene.String(required=True)

    def mutate(self, info, user_id, token):
        user = User.objects.get(pk=user_id)
        access_token = AccessToken.objects.create(user=user, token=token)
        return CreateAccessToken(access_token=access_token)

class CreateRefreshToken(graphene.Mutation):
    refresh_token = graphene.Field(RefreshTokenType)

    class Arguments:
        user_id = graphene.Int(required=True)
        token = graphene.String(required=True)

    def mutate(self, info, user_id, token):
        user = User.objects.get(pk=user_id)
        refresh_token = RefreshToken.objects.create(user=user, token=token)
        return CreateRefreshToken(refresh_token=refresh_token)

class Mutation(ObjectType):
    create_access_token = CreateAccessToken.Field()
    create_refresh_token = CreateRefreshToken.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](http://127.0.0.1:8000/static/signin_schema.md)
"""
