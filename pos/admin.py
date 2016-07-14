from django.contrib import admin

from imagekit.admin import AdminThumbnail
from models import Table, Category, Product, Order, Bill


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='image_thumb')


admin.site.register(Table)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Bill)
