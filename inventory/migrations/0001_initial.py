# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('department', models.IntegerField(choices=[(0, 'Kitchen'), (1, 'Bar')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('unit_price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('catgory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Out Of Stock'), (1, 'Recived')], default=0)),
                ('Notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
