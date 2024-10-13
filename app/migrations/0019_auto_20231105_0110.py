# Generated by Django 3.2.21 on 2023-11-04 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_registrations_started_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contests',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='admins',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.DeleteModel(
            name='Admin_contests',
        ),
    ]