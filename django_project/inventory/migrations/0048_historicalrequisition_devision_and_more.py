# Generated by Django 4.1.10 on 2023-08-01 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_approvals'),
        ('inventory', '0047_remove_assigned_assets_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrequisition',
            name='devision',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='company.devision'),
        ),
        migrations.AddField(
            model_name='historicalrequisition',
            name='sub_division',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='company.sub_devision'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='devision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reqdevisions', to='company.devision'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='sub_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reqsub_districts', to='company.sub_devision'),
        ),
    ]
