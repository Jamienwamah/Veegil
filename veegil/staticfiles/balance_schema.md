# Account Model

Description:
The Account model represents a user's account with their balance.

### Fields
- `id`: The unique identifier for the account.
- `user`: The user associated with the account.
- `balance`: The current balance in the account.

### Model Definition

```python
from djongo import models

class Account(models.Model):
    user = models.OneToOneField('signup.User', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        db_table = 'account'
