# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_item_publish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='log',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
