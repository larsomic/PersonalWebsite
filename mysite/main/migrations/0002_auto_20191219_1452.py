# Generated by Django 2.2.6 on 2019-12-19 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 14, 52, 57, 56906), verbose_name='date published'),
        ),
    ]
