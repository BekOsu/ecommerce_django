# Generated by Django 4.0.2 on 2022-03-27 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_test_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='create',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(),
        ),
    ]
