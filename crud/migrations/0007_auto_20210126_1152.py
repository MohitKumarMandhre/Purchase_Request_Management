# Generated by Django 3.1.5 on 2021-01-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_auto_20210126_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveorder',
            name='quantity',
            field=models.FloatField(default=1, null=True),
        ),
    ]