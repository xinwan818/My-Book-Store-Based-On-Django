# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20170523_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='Not_avaliable_day',
            field=models.IntegerField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], max_length=10, null=True),
        ),
    ]