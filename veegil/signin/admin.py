from django.contrib import admin
from .models import AccessToken, RefreshToken

# Register your models here.

admin.site.register(AccessToken)
admin.site.register(RefreshToken)
