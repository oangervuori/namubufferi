# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-29 22:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('namubufferiapp', '0009_auto_20170214_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='magic_token',
            field=models.CharField(blank=True, max_length=44, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='magic_token_ttl',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 29, 22, 26, 2, 902137, tzinfo=utc)),
        ),
    ]
