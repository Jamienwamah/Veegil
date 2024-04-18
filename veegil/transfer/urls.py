from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from . import views

urlpatterns = [
    path('transfer-money/', views.transfer_money, name='transfer_money'),
    path('transfergraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
