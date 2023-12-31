# Generated by Django 4.1.10 on 2023-10-05 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_devision_code_sub_devision_code'),
        ('accounting', '0030_paymentvoucher_approved_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pveligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ia_date', models.DateField(blank=True, null=True)),
                ('ia_code', models.CharField(blank=True, max_length=250, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('withholding_tax', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100)),
                ('withholding_tax_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('devision', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iadevisions', to='company.devision')),
                ('pv_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pvinternal', to='accounting.paymentvoucher')),
                ('sub_division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iasub_districts', to='company.sub_devision')),
            ],
            options={
                'verbose_name': 'Pveligibility',
                'verbose_name_plural': 'Pveligibility',
                'db_table': 'Pveligibility',
            },
        ),
    ]
