from django.urls import path
from .views import ProfileView
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profiles'),
    path('profilegraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

