# Generated by Django 4.0.1 on 2024-04-30 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0015_alter_otp_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp_code',
            field=models.CharField(default='5644', max_length=6),
        ),
    ]
