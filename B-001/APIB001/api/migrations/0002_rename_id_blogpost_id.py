# Generated by Django 5.0.1 on 2024-02-02 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='id',
            new_name='ID',
        ),
    ]
