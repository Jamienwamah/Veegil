# Generated by Django 4.1.13 on 2024-04-17 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
        ('otp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otps', to='signup.user'),
        ),
    ]
