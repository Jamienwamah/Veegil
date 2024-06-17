from django.db import models
from django.utils import timezone
from signup.models import User
import uuid

class Withdraw(models.Model):
    user = models.ForeignKey(User, related_name='withdraws', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=15, unique=True, default=uuid.uuid4) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, default='withdraw')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Withdrawal #{self.pk}"

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except IntegrityError as e:
            if 'unique constraint' in str(e):
                return 'Error: Withdrawal with the same account number already exists'
            else:
                return 'Error: An error occurred while saving the withdrawal'
