# Generated by Django 3.1.5 on 2021-01-28 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_saveorder_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentName', models.CharField(max_length=252)),
                ('documentDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('itemName', models.CharField(max_length=200)),
                ('make', models.CharField(default='number', max_length=100)),
                ('UOM', models.CharField(max_length=100, null=True)),
                ('quantity', models.FloatField(default=1, null=True)),
                ('rate', models.FloatField(null=True)),
                ('amount', models.FloatField(null=True)),
                ('requiredOn', models.DateField(null=True)),
                ('remarks', models.TextField()),
            ],
        ),
    ]