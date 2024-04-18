from django.urls import path
from .views import BalanceAPIView

urlpatterns = [
    path('balance/', BalanceAPIView.as_view(), name='balance')
]
