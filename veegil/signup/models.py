from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from .managers import UserManager
import uuid

 
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    verification_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number_regex = RegexValidator(
        regex=r'^[1-9]\d{9}$', message=_("Phone number must start with a digit other than 0 and have a length of 10 digits."))
    phone_number = models.CharField(validators=[
        phone_number_regex], max_length=15, unique=True, verbose_name=_('Phone Number'), blank=True)
    password = models.CharField(max_length=255, verbose_name=_('Password'), blank=True)
    password2 = models.CharField(max_length=255, verbose_name=_('Password2'), blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    residential_address = models.TextField(
        verbose_name=_('Residential Address'), blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'password', 'password2']
    
    objects = UserManager()
    
    def __str__(self):
        return "%s"%(self.email)
    
    @property
    def get_full_name(self):
        return f"{self.first_name}, {self.last_name}"
    
    def tokens(self):
        pass
    
    