# Generated by Django 4.1.10 on 2023-07-14 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_district_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='district',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='authentication.district'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='region',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='authentication.region'),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='authentication.district'),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='authentication.region'),
        ),
    ]
