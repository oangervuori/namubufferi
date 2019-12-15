# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-18 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('namubufferiapp', '0010_auto_20171029_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertag',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='magic_token_ttl',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 18, 16, 40, 30, 400931, tzinfo=utc)),
        ),
    ]