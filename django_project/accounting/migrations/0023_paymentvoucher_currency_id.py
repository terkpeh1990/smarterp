# Generated by Django 4.1.10 on 2023-09-27 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0022_paymentvoucher_withholding_tax_amount_pvdetail_pv_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentvoucher',
            name='currency_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pvcurrency', to='accounting.currency'),
        ),
    ]
