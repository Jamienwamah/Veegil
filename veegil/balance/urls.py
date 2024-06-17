from django.urls import path
from .views import BalanceAPIView
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('balance/', BalanceAPIView.as_view(), name='balance'),
    path('balancegraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
