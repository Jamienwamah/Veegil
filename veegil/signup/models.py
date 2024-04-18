from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import uuid

class CustomAppUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

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
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'), null=True, blank=True)
    password = models.CharField(max_length=255, verbose_name=_('Password'), blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    residential_address = models.TextField(verbose_name=_('Residential Address'), blank=True)
    referral_code = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Referral Code'))
    wallet_address = models.CharField(max_length=36, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    account_number = models.CharField(max_length=15, unique=True, verbose_name=_('Account Number'), blank=True, default=uuid.uuid4())

    objects = CustomAppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(Group, related_name='customappuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_app_user_permissions', blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.account_number = self.generate_account_number()
        super().save(*args, **kwargs)

    def generate_account_number(self):
        # Generate a unique account number based on UUID
        return uuid.uuid4().hex[:10]

    def __str__(self):
        return self.username
