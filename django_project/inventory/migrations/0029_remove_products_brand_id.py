# Generated by Django 4.1.10 on 2023-07-26 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0028_job_detail_brand_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='brand_id',
        ),
    ]
