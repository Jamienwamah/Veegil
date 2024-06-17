from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from .views import DepositAPIView

urlpatterns = [
    path('deposit/', DepositAPIView.as_view(), name='deposit'),
    path('depositgraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
