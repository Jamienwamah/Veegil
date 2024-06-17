from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from . import views

urlpatterns = [
    path('transaction-history/', views.transaction_history, name='transaction_history'),
    path('transactionhistorygraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
