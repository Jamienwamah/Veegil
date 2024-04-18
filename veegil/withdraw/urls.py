from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from .views import Withdraw


urlpatterns = [
    path('withdraw/', Withdraw.as_view(), name='withdraw'),
    path('withdrawgraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
