# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20170523_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='plan',
            name='Not_avaliable_day',
            field=models.CharField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='plan',
            field=models.ManyToManyField(to='books.Plan', verbose_name='Unavailable Time'),
        ),
    ]
