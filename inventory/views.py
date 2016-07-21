from django.shortcuts import render
from django.views.generic.list import ListView
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
