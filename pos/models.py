from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Table(models.Model):
    number = models.PositiveIntegerField()
    notes = models.CharField(max_length=255, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    department = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    price = models.PositiveIntegerField()
    catgory = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images')
    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality':60})
    added = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)


class Order(models.Model):
    number = models.PositiveIntegerField()
    table = models.ForeignKey(Table)
    product = models.ForeignKey(Product)
    amount = models.PositiveIntegerField()
    notes = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)


class Bill(models.Model):
    order = models.ForeignKey(Order)
    table = models.ForeignKey(Table)
    total = models.PositiveIntegerField()
    transaction_type = models.BooleanField()
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
