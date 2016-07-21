from __future__ import unicode_literals

from django.db import models
#from orders.models import Order


class DateTimeStamp(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Table(DateTimeStamp):
    number = models.PositiveIntegerField()
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return str(self.number)


# class Bill(DateTimeStamp):
#     order = models.ForeignKey(Order)
#     table = models.ForeignKey(Table)
#     total = models.PositiveIntegerField()
#     transaction_type = models.BooleanField()
