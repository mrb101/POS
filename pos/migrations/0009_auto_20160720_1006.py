# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_shopping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]