from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class DateTimeStamp(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Category(DateTimeStamp):
    DEPARTMENT = ((0, 'Kitchen'), (1, 'Bar'))
    slug = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    department = models.IntegerField(blank=False,
                                     null=False,
                                     choices=DEPARTMENT)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"self": self.slug})

    @property
    def get_department(self):
        if self.department == 0:
            return "Kitchen"
        else:
            return "Bar"


class Product(DateTimeStamp):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    unit_price = models.PositiveIntegerField()
    catgory = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images', blank=True)
    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 60})

    def __unicode__(self):
        return self.title

    @property
    def is_available(self):
        if self.available == True:
            return "available"
        else:
            return "Out Of Stock"


class Shopping(DateTimeStamp):
    STATUS = ((0, 'Out Of Stock'), (1, 'Recived'))
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.IntegerField(default=0, choices=STATUS)
    Notes = models.TextField()

    def __unicode__(self):
        return self.item
