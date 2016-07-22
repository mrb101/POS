# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from models import Product, Shopping, Category


class ProductList(ListView):
    model = Product
    template_name = 'inventory/menu.html'


class ShoppingList(ListView):
    model = Shopping
    template_name = 'inventory/shopping_list.html'


class CategoryList(ListView):
    model = Category
    template_name = 'inventory/category_list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'inventory/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetail, self).get_context_data(*args, **kwargs)
        category = self.get_object()
        products = category.product_set.all()
        context['products'] = products
        return context
