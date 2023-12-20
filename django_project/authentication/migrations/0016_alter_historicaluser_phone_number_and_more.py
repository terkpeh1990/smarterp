# Generated by Django 4.1.10 on 2023-07-15 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_historicaluser_staffid_alter_user_staffid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must begin with 0 and contain only 10 digits', regex='^(0)\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must begin with 0 and contain only 10 digits', regex='^(0)\\d{9}$')]),
        ),
    ]
