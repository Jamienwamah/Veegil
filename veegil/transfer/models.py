from django.db import models
from django.utils import timezone
from signup.models import User

class Transfer(models.Model):
    sender = models.ForeignKey(User, related_name='sent_transfer', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_transfer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, default='transfer')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transaction #{self.pk}"
