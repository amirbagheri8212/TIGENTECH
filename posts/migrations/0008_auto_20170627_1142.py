# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170627_1139'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]
