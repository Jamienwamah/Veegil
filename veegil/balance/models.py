from django.db import models

class Account(models.Model):
    user = models.OneToOneField('signup.User', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        db_table = 'account'
