# Generated by Django 3.0.7 on 2020-07-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subContent',
            field=models.TextField(default='', verbose_name='Sub_Content'),
            preserve_default=False,
        ),
    ]