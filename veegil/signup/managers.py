from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please input a valid email"))

    def create_user(self, first_name, last_name, username, email, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_verified", False)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is True:
            raise ValueError(_("Is staff must be false for all users"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email is required"))

        if not first_name:
            raise ValueError(_("First name is required"))

        if not last_name:
            raise ValueError(_("Last name is required"))

        if not username:
            raise ValueError(_("Username must be entered"))

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, username, email, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Is staff must be true for all users"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Is superuser must be true for all users"))

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone_number=phone_number,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user
