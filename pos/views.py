from django.shortcuts import render
from models import Table, Product, Order, Bill


def menu(request):
    template = 'pos/menu.html'
    context = {}
    return render(request, template, context)


def index(request):
    template = 'pos/index.html'
    context = {}
    return render(request, template, context)


def cash(request):
    template = 'pos/cash.html'
    context = {}
    return render(request, template, context)


def kitchen(request):
    template = 'pos/kitchen.html'
    context = {}
    return render(request, template, context)


def bar(request):
    template = 'pos/bar.html'
    context = {}
    return render(request, template, context)


def table(request):
    template = 'pos/bar.html'
    context = {}
    return render(request, template, context)


def checkout(request):
    template = 'pos/checkout.html'
    context = {}
    return render(request, template, context)
