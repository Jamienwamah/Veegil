import graphene
from graphene_django.types import DjangoObjectType
from graphql.utilities import print_schema
from .models import OTP

class OTPType(DjangoObjectType):
    class Meta:
        model = OTP

class Query(graphene.ObjectType):
    otps = graphene.List(OTPType)

    def resolve_otps(self, info):
        return OTP.objects.all()


class CreateOTP(graphene.Mutation):
    otp = graphene.Field(OTPType)

    class Arguments:
        user_id = graphene.Int()

    def mutate(self, info, user_id):
        user = User.objects.get(pk=user_id)
        otp = OTP(user=user)
        otp.generate_and_encrypt_otp()
        return CreateOTP(otp=otp)

class VerifyOTP(graphene.Mutation):
    is_valid = graphene.Boolean()

    class Arguments:
        otp_code = graphene.String()
        otp_id = graphene.Int()

    def mutate(self, info, otp_code, otp_id):
        otp = OTP.objects.get(pk=otp_id)
        is_valid = otp.verify_otp(otp_code)
        return VerifyOTP(is_valid=is_valid)

class Mutation(graphene.ObjectType):
    create_otp = CreateOTP.Field()
    verify_otp = VerifyOTP.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](http://127.0.0.1:8000/static/otp_schema.md)
"""

# Finally, pass the schema string to GraphQL Playground
# You can use the `schema` parameter if you are using GraphQL Playground programmatically,
# or simply paste the `schema_str` into the GUI if you are using it interactively.
