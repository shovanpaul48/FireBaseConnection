# Generated by Django 5.0.3 on 2024-03-20 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='document',
            new_name='documents',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='link',
            new_name='links',
        ),
    ]