from rest_framework import serializers
from .models import TransactionHistory

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'
