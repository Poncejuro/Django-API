# Generated by Django 5.0.1 on 2024-02-03 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_fecha_cryptocurrencyhistory_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrencyhistory',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cryptocurrency'),
        ),
    ]