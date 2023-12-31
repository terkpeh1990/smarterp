# Generated by Django 4.1.10 on 2023-07-26 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_restock_details_restock_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_certification',
            name='classification',
        ),
        migrations.AddField(
            model_name='job_certification',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.products'),
        ),
        migrations.AddField(
            model_name='job_detail',
            name='describtion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='job_detail',
            name='restock_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.restocks'),
        ),
    ]
