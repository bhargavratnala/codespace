# Generated by Django 3.2.21 on 2023-09-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230924_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='contest_code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]