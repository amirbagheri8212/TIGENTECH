# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 09:16
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=5000)),
                ('continent', models.CharField(choices=[('Asia', 'Asia')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('PictureFile', models.ImageField(upload_to='')),
                ('Bio', ckeditor.fields.RichTextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quote.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', ckeditor.fields.RichTextField()),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quote.Person')),
            ],
        ),
    ]
