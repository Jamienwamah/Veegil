from . import views
from .schema import schema
from graphene_django.views import GraphQLView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("auth/login/", views.LoginView.as_view(), name="login"),
    path("auth/jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("auth/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('logingraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]