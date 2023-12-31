# Generated by Django 4.1.10 on 2023-07-28 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_approvals'),
        ('inventory', '0038_alter_requisition_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrequisition',
            name='tenant_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='company.tenants'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='tenant_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='req', to='company.tenants'),
        ),
    ]
