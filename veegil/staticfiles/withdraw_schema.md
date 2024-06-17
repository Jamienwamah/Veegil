# Withdraw Model

Description:
The Withdraw model represents withdrawals made by users.

### Fields
- `id`: The unique identifier for the withdrawal.
- `user`: The user who made the withdrawal.
- `account_number`: The account number associated with the withdrawal.
- `amount`: The amount withdrawn.
- `type`: The type of withdrawal (default: "withdraw").
- `timestamp`: The timestamp of the withdrawal.

### Model Definition

```python
from django.db import models
from django.utils import timezone
from signup.models import User
import uuid

class Withdraw(models.Model):
    user = models.ForeignKey(User, related_name='withdraws', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=15, unique=True, default=uuid.uuid4()) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, default='withdraw')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Withdrawal #{self.pk}"
