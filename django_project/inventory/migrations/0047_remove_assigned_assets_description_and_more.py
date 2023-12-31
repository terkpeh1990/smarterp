# Generated by Django 4.1.10 on 2023-07-31 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0046_assigned_assets_tenant_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigned_assets',
            name='description',
        ),
        migrations.RemoveField(
            model_name='assigned_assets',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='assigned_assets',
            name='user',
        ),
        migrations.AddField(
            model_name='assigned_assets',
            name='pool',
            field=models.BooleanField(default=False),
        ),
    ]
