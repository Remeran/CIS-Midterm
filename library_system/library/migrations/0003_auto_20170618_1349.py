# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 13:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20170618_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_passed',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]