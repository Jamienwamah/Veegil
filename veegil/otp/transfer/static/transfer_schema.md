# Transfer Model

Description:
The Transfer model represents transfers of funds between users.

### Fields
- `id`: The unique identifier for the transfer.
- `sender`: The user who initiated the transfer.
- `receiver`: The user who received the transfer.
- `amount`: The amount of funds transferred.
- `type`: The type of transfer (default: "transfer").
- `timestamp`: The timestamp of the transfer.

### Model Definition

```python
from django.db import models
from django.utils import timezone
from signup.models import User

class Transfer(models.Model):
    sender = models.ForeignKey(User, related_name='sent_transfer', on_delete=models.CASCADE)
