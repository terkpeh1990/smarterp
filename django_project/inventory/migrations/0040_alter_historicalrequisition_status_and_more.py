# Generated by Django 4.1.10 on 2023-07-28 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0039_historicalrequisition_tenant_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrequisition',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Awaiting Approval', 'Awaiting Approval'), ('Issued', 'Issued'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Awaiting Approval', 'Awaiting Approval'), ('Issued', 'Issued'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20, null=True),
        ),
    ]
