# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20170501_2245'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='MyUser',
        ),
    ]