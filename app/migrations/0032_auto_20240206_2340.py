# Generated by Django 3.2.21 on 2024-02-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_contests_reg_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrations',
            name='last_que_no',
            field=models.IntegerField(default=0, help_text='last solved que'),
        ),
        migrations.AddField(
            model_name='registrations',
            name='que_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]