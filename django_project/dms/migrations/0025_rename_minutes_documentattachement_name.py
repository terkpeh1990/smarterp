# Generated by Django 4.1.10 on 2023-09-12 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0024_remove_documentbudget_currency_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentattachement',
            old_name='minutes',
            new_name='name',
        ),
    ]
