# Generated by Django 3.1.1 on 2020-09-11 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 20, 28, 14, 58235)),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 20, 28, 14, 58235)),
        ),
    ]