from django.urls import path
from .views import RegisterUserView
from .schema import schema
from graphene_django.views import GraphQLView
from . import views

urlpatterns = [
    #path('auth/register-otp/', RegisterUserView.as_view(), name='register_user'),
    path('auth/resend-otp/', RegisterUserView.as_view(), name='resend-otp'),
    path('verify-register-otp/', views.verify_otp, name='verify_otp'),
    path('otpgraphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

