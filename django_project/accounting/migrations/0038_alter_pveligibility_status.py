# Generated by Django 4.1.10 on 2023-10-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0037_alter_paymentvoucher_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pveligibility',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled')], default='Completed', max_length=60),
        ),
    ]
