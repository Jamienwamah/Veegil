import graphene
from graphene_django import DjangoObjectType
from graphql.utilities import print_schema
from .models import Profile

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

class Query(graphene.ObjectType):
    profiles = graphene.List(ProfileType)

    def resolve_profiles(self, info):
        return Profile.objects.all()

class CreateProfile(graphene.Mutation):
    full_name = graphene.String()
    bio = graphene.String()
    image = graphene.String()
    verified = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, full_name, bio, image, verified):
        profile = Profile.objects.create(
            full_name=full_name,
            bio=bio,
            image=image,
            verified=verified
        )
        return CreateProfile(
            full_name=profile.full_name,
            bio=profile.bio,
            image=profile.image,
            verified=profile.verified
        )

class Mutation(graphene.ObjectType):
    create_profile = CreateProfile.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

schema_str = print_schema(schema.graphql_schema)
print(schema_str)
schema_str += """
# For documentation on how to use this API, please refer to [API Documentation](https://bankapp-hd3c.onrender.com/static/profile_schema.md)
"""



