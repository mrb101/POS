from __future__ import unicode_literals

from django.db import models

from inventory.models import Product
from pos.models import Table


class DateTimeStamp(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Order(DateTimeStamp):
    ORDER_STATUS = ((0, 'On Going'), (1, 'Hold'), (2, 'Paid'))
    number = models.PositiveIntegerField()
    table = models.ForeignKey(Table)
    status = models.IntegerField(default=0, choices=ORDER_STATUS)
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.number)

    @property
    def get_status(self):
        if self.status == 0:
            return "On Going"
        elif self.status == 1:
            return "On Hold"
        else:
            return "Order Paid"

class OrderItem(DateTimeStamp):
    STATUS = ((0, 'Preparing'), (1, 'Served'))
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    table = models.ForeignKey(Table)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    notes = models.TextField()
    status = models.IntegerField(default=0, choices=STATUS)

    def __unicode__(self):
        return str(self.product)

    @property
    def get_status(self):
        if self.status == 0:
            return "Preparing"
        else:
            return "Served"
