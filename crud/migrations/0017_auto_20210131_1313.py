# Generated by Django 3.1.5 on 2021-01-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_remove_set_arr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='remarks',
            field=models.TextField(null=True),
        ),
    ]
