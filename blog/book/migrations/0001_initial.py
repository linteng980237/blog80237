# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('author', models.CharField(max_length=128)),
                ('publisher', models.CharField(max_length=128)),
                ('time', models.DateField()),
                ('version', models.CharField(max_length=128)),
            ],
        ),
    ]
