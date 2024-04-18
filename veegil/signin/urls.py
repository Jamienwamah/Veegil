from django.urls import path
from  signin.views import LoginView

#Create urls here

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
]
