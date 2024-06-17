# user/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User  # Import UserProfile model

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)