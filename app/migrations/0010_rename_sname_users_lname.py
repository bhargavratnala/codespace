# Generated by Django 3.2.21 on 2023-10-04 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_users_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='sname',
            new_name='lname',
        ),
    ]