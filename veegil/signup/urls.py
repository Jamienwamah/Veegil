from django.urls import path
from .views import CustomUserAPIView
from .schema import schema
from graphene_django.views import GraphQLView


urlpatterns = [
    path('auth/register/', CustomUserAPIView.as_view(), name='register'),
    path('registergraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]