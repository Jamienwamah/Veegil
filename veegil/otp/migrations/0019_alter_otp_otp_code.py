# Generated by Django 4.0.1 on 2024-05-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0018_alter_otp_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp_code',
            field=models.CharField(default='4916', max_length=6),
        ),
    ]
