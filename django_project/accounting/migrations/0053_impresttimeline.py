# Generated by Django 4.1.10 on 2023-10-23 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting', '0052_imprest_approved_rank_imprest_approved_sub_division_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impresttimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.CharField(blank=True, max_length=255, null=True)),
                ('timeline_comment', models.CharField(blank=True, max_length=255, null=True)),
                ('timelinedate', models.DateTimeField(auto_now_add=True)),
                ('imprest_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='impresttimeline', to='accounting.imprest')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Impresttimeline',
                'verbose_name_plural': 'Impresttimelines',
                'db_table': 'Impresttimelines',
            },
        ),
    ]
