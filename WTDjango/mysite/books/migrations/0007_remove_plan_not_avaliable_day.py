# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20170523_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='Not_avaliable_day',
        ),
    ]
