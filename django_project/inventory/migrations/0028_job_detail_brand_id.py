# Generated by Django 4.1.10 on 2023-07-26 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_rename_describtion_job_detail_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_detail',
            name='brand_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.brands'),
        ),
    ]
