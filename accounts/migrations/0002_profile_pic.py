# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
