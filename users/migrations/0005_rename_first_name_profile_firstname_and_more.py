# Generated by Django 4.1.6 on 2023-04-22 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usermodel_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='last_name',
            new_name='lastname',
        ),
    ]