# Generated by Django 4.2.7 on 2024-08-23 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='contry',
            new_name='country',
        ),
    ]
