# Generated by Django 3.0.7 on 2020-07-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20200715_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=50, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]