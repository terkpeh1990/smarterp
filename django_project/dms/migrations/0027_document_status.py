# Generated by Django 4.1.10 on 2023-09-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0026_alter_documentattachement_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
