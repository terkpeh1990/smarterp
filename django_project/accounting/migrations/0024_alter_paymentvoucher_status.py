# Generated by Django 4.1.10 on 2023-09-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0023_paymentvoucher_currency_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentvoucher',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Approved', 'Approved'), ('Authorised', 'Authorised'), ('Authorised & Passed', 'Authorised & Passed'), ('Check No Entered', 'Check No Entered'), ('Pv Eligibility', 'Pv Eligibility'), ('Paid', 'Paid')], default='Pending', max_length=100),
        ),
    ]
