# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachprogramming', '0002_auto_20170625_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
