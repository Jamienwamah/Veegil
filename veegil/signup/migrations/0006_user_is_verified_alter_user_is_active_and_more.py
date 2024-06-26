# Generated by Django 4.0.1 on 2024-04-29 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_remove_user_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
