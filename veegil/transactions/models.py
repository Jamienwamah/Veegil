from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from signup.models import User

class TransactionHistory(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('transfer', 'Transfer'),
    ]

    user = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transaction #{self.pk}"


    def save(self, *args, **kwargs):
        try:
            self.clean()  
            super().save(*args, **kwargs)  
        except ValidationError as e:
            raise ValidationError(e.message_dict)
        except Exception as e:
            raise e
