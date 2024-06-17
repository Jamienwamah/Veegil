# Transaction Model

Description:
The Transaction model represents financial transactions between users.

### Fields
- `id`: The unique identifier for the transaction.
- `sender`: The user who sent the transaction.
- `receiver`: The user who received the transaction.
- `amount`: The amount of the transaction.
- `type`: The type of transaction (e.g., deposit, withdraw, transfer).
- `timestamp`: The timestamp of the transaction.

### Model Definition

```python
from django.db import models
from django.utils import timezone
from signup.models import User

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
