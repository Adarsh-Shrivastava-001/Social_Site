# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180619_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_published',
            field=models.DateField(default=None, null=True),
        ),
    ]