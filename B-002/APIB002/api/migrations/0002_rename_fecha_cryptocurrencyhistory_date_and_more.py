# Generated by Django 5.0.1 on 2024-02-02 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptocurrencyhistory',
            old_name='fecha',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='cryptocurrencyhistory',
            old_name='precio',
            new_name='price',
        ),
    ]