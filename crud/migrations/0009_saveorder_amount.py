# Generated by Django 3.1.5 on 2021-01-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_auto_20210126_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveorder',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]
