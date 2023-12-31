# Generated by Django 4.1.10 on 2023-07-25 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_supplier_restocks_supplier_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restock_details',
            options={'permissions': [('custom_create_restock_detail', 'Can Create Restock Detail'), ('custom_update_restock_detail', 'Can Update Restock Detail'), ('custom_delete_restock_detail', 'Can Delete Restock Detail'), ('custom_view_restock_detail', 'Can View Restock Detail')], 'verbose_name': 'Restock_detail', 'verbose_name_plural': 'Restock_details'},
        ),
        migrations.AlterModelOptions(
            name='restocks',
            options={'permissions': [('custom_create_restock', 'Can Create Restock'), ('custom_update_restock', 'Can Update Restock'), ('custom_delete_restock', 'Can Delete Restock'), ('custom_view_restock', 'Can View Restock')], 'verbose_name': 'Restock', 'verbose_name_plural': 'Restocks'},
        ),
        migrations.AlterModelTable(
            name='restock_details',
            table='Restock_detail',
        ),
        migrations.AlterModelTable(
            name='restocks',
            table='Restock',
        ),
    ]
