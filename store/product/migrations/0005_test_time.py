# Generated by Django 4.0.2 on 2022-03-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
