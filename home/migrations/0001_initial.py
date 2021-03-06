# Generated by Django 3.0.7 on 2020-07-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('website', models.CharField(max_length=50, verbose_name='Website')),
                ('msg', models.TextField(verbose_name='Text_Field')),
            ],
        ),
    ]
