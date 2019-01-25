# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-24 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20180619_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='disliked_by',
            field=models.ManyToManyField(related_name='dislike_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posts',
            name='liked_by',
            field=models.ManyToManyField(related_name='like_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
