# Generated by Django 3.0.7 on 2020-07-15 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='timeStamp'),
        ),
    ]