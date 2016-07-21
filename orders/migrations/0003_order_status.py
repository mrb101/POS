# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'On Going'), (1, 'Hold'), (2, 'Paid')], default=0),
        ),
    ]
