import graphene
from graphene import List
from graphene_django.types import DjangoObjectType
from graphql.utilities import print_schema
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        date_of_birth = graphene.Date()
        gender = graphene.String()
        residential_address = graphene.String()
        referral_code = graphene.String()
        is_active = graphene.Boolean()
        is_staff = graphene.Boolean()
        phone_number = graphene.String()

    def mutate(self, info, first_name, last_name, username, email, **kwargs):
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            **kwargs
        )
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](http://127.0.0.1:8000/static/signup_schema.md)
"""
