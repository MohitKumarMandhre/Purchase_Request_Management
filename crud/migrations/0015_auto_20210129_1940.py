# Generated by Django 3.1.5 on 2021-01-29 14:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0014_set_v1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='v1',
        ),
        migrations.AddField(
            model_name='set',
            name='arr',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
