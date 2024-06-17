from django.db import models
from django.utils import timezone
from signup.models import User
from django.db.utils import IntegrityError

class Transfer(models.Model):
    user = models.ForeignKey(User, related_name='sent_transfer', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_transfer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, default='transfer')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transfer #{self.pk}"

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except IntegrityError as e:
            # Handle integrity errors (e.g., duplicate entries, foreign key constraints)
            return f"Error saving Transfer: {e}"
