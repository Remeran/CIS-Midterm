# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_passed',
            field=models.DurationField(),
        ),
    ]
