# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20170501_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(default=18825145679, verbose_name=b'phone'),
        ),
    ]
