# Generated by Django 4.1.10 on 2023-10-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0048_paymentvoucherbeneficiary_comfirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payables',
            name='status',
            field=models.CharField(choices=[('Awaiting Payment', 'Awaiting Payment'), ('Recipients Notified', 'Recipients Notified'), ('Amount Paid', 'Amount Paid')], default='Awaiting Payment', max_length=60),
        ),
    ]
