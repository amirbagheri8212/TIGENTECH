# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.CharField(choices=[('Asia', 'Asia'), ('America', 'America')], default='', max_length=1000),
            preserve_default=False,
        ),
    ]
