# Generated by Django 4.0.1 on 2024-04-28 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
        ('balance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='signup.user'),
        ),
    ]
