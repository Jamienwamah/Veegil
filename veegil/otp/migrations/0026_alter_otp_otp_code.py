# Generated by Django 4.0.1 on 2024-05-02 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0025_alter_otp_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp_code',
            field=models.CharField(default='7188', max_length=6),
        ),
    ]
