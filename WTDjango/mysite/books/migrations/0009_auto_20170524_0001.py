# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_plan_not_avaliable_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='Not_avaliable_day',
            field=models.IntegerField(blank=True, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], null=True),
        ),
    ]