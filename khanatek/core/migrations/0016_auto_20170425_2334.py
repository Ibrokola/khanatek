# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-26 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20170424_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='articlepage',
            name='streamfield',
        ),
    ]
