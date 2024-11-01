# Generated by Django 3.2.21 on 2024-01-27 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_contests_contest_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeDuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online', models.IntegerField(default=0, help_text='0=ofline, 1=online')),
                ('in_duel', models.IntegerField(default=0, help_text='0=not in duel, 1=in duel')),
                ('opponent', models.CharField(max_length=30, unique=True)),
                ('user_level', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_active_time', models.DateTimeField(auto_now=True)),
                ('contest_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.contests')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.users')),
            ],
        ),
    ]
