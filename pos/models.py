from __future__ import unicode_literals

from django.db import models


class Table(models.Model):
    number = models.PositiveIntegerField()
    notes = models.CharField(max_length=255, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    department = models.CharField(max_length=255, blank=False, null=False)


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    price = models.PositiveIntegerField()
    catgory = models.ForeignKey(Category)
    # image for later


class Order(models.Model):
    number = models.PositiveIntegerField()
    table = models.ForeignKey(Table)
    product = models.ForeignKey(Product)
    amount = models.PositiveIntegerField()
    notes = models.CharField(max_length=255, blank=True, null=True)
    # datetime


class Bill(models.Model):
    order = models.ForeignKey(Order)
    table = models.ForeignKey(Table)
    total = models.PositiveIntegerField()
    transaction_type = models.BooleanField()
