# Generated by Django 4.1.10 on 2023-09-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0006_remove_documentdestination_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentattachement',
            name='minutes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
