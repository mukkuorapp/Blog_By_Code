# Generated by Django 3.0.7 on 2020-07-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20200717_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Views on Post'),
        ),
    ]
