import graphene
from graphene import List
from graphene_django.types import DjangoObjectType
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

schema = graphene.Schema(query=Query)
