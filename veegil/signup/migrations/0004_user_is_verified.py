# Generated by Django 4.0.1 on 2024-04-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
