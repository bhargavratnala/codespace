# Generated by Django 3.2.21 on 2023-09-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230924_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mcq',
            old_name='op1',
            new_name='options',
        ),
        migrations.RemoveField(
            model_name='mcq',
            name='op2',
        ),
        migrations.RemoveField(
            model_name='mcq',
            name='op3',
        ),
        migrations.RemoveField(
            model_name='mcq',
            name='op4',
        ),
        migrations.AlterField(
            model_name='contests',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
        migrations.AlterField(
            model_name='contests',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='status',
            field=models.CharField(default='draft', max_length=15),
        ),
        migrations.AlterField(
            model_name='contests',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='user_profile_pics'),
        ),
    ]