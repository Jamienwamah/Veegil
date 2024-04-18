import graphene
from graphene import List
from graphene_django.types import DjangoObjectType
from .models import OTP

class OtpType(DjangoObjectType):
    class Meta:
        model = OTP

class Query(graphene.ObjectType):
    otps = List(OtpType)

    def resolve_otps(self, info):  # Corrected method name
        return OTP.objects.all()

schema = graphene.Schema(query=Query)
