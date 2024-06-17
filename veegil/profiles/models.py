from django.db import models
from signup.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_image", default="default.jpg")
    verified = models.BooleanField(default=False)