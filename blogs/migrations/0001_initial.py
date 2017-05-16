# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 13:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name=b'title')),
                ('content', models.TextField(verbose_name=b'content')),
                ('views', models.IntegerField(default=0, verbose_name=b'views')),
                ('reply_count', models.IntegerField(default=0, verbose_name=b'reply count')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'published date')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name=b'edited date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name=b'content')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'published date')),
                ('article', models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='blogs.Article', verbose_name=b'Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
