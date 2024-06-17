## Deposit Model

### Description
The `Deposit` model represents deposits made by users.

### Fields
- `id`: The unique identifier for the deposit.
- `user`: The user who made the deposit.
- `amount`: The amount deposited.
- `account_number`: The account number associated with the deposit.
- `type`: The type of deposit.
- `timestamp`: The timestamp of the deposit.

### Model Definition

```python
from django.db import models
from django.utils import timezone
from signup.models import User
import uuid

class Deposit(models.Model):
    user = models.ForeignKey(User, related_name='deposit', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.UUIDField(default=uuid.uuid4())
    type = models.CharField(max_length=20, default='deposit')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Deposit #{self.pk} by {self.user.username}"
