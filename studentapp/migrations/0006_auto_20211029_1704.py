# Generated by Django 3.2.8 on 2021-10-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_auto_20211029_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattend',
            name='atten_date',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='studentattend',
            name='in_time',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='studentattend',
            name='out_time',
            field=models.CharField(max_length=12),
        ),
    ]