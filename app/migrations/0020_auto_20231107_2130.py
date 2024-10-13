# Generated by Django 3.2.21 on 2023-11-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20231105_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest_question',
            name='mcq_id',
        ),
        migrations.AddField(
            model_name='questions',
            name='correct_op',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='que_typ',
            field=models.IntegerField(default=0, help_text='0=coding, 1=mcq'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='level',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='outputs',
            field=models.FileField(blank=True, null=True, upload_to='outputs'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='solution',
            field=models.FileField(blank=True, null=True, upload_to='solutions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='tc_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='testcases',
            field=models.FileField(blank=True, null=True, upload_to='testcases'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='tle',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Mcq',
        ),
    ]