# Generated by Django 4.1.10 on 2023-09-26 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0016_imprest_devision_imprest_sub_division_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentvoucher',
            options={'permissions': [('custom_create_pv', 'Can Create PV'), ('custom_update_pv', 'Can Update PV'), ('custom_delete_pv', 'Can Delete PV '), ('custom_view_pv', 'Can View PV'), ('custom_approve_pv', 'Can Approve PV'), ('custom_authorise_pv', 'Can Authorise PV '), ('custom_authorise_annd_pass_pv', 'Can Authorise and pass PV '), ('custom_pay_pv', 'Can Pay PV'), ('custom_add_cheque_no', 'Can Add Cheque No'), ('custom_pay_impress', 'Can Pay Impress')], 'verbose_name': 'PaymentVoucher', 'verbose_name_plural': 'PaymentVoucher'},
        ),
    ]
