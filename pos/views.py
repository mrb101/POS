from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from models import Table
from inventory.models import Product, Shopping
from orders.models import Order, OrderItem
from forms import LoginForm, OrderForm, PaymentForm, ShoppingForm


def login_view(request):
    template = 'pos/login.html'
    form = LoginForm
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "You have logged in!")
                return redirect(request.GET.get('next') or 'home')
            else:
                messages.warning(request, "Your account is disabled!")
                return redirect('/login')
        else:
            messages.warning(request, "The username or password are not valid!")
            return redirect('/login')
    context = {'form': form}
    return render(request, template, context)


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('home')


def menu(request):
    template = 'pos/menu.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template, context)


class HomePage(TemplateView):
    template_name = 'pos/index.html'
    context = {}


def index(request):
    template = 'pos/index.html'
    context = {}
    return render(request, template, context)


class TableList(ListView):
    model = Table
    template_name = 'pos/table_list.html'
    context_object_name = 'tables'


@login_required(login_url='/login')
def kitchen(request):
    template = 'pos/kitchen.html'
    food = OrderItem.objects.filter(product__catgory=1).order_by('-created')
    context = {'food': food}
    return render(request, template, context)


@login_required(login_url='/login')
def bar(request):
    template = 'pos/bar.html'
    drink = OrderItem.objects.filter(product__catgory__gt=1).order_by('-created')
    context = {'drink': drink}
    return render(request, template, context)


@login_required(login_url='/login')
def table(request, pk):
    table = pk
    history = Order.objects.filter(table=pk)
    template = 'pos/tables.html'
    try:
        order = Order.objects.filter(table=pk).latest('created')
        if order.status == 2:
            order = None
    except Order.DoesNotExist:
        order = None
    items = OrderItem.objects.filter(order=order)
    context = {'order': order,
               'items': items,
               'table': table,
               'history': history}
    return render(request, template, context)


@login_required(login_url='/login')
def checkout(request, pk):
    template = 'pos/checkout.html'
    form = PaymentForm()
    table = pk
    try:
        order = Order.objects.filter(table=table).latest('created')
    except Order.DoesNotExist:
        order = None
    if order == None or order.paid == True:
        messages.success(request, "No open orders on this table")
        return redirect("/cash")
    elif order.paid == False:
        orders = OrderItem.objects.filter(order=order)
        total = 0
        for item in orders:
            total += item.total_price
    pay_form = PaymentForm(request.POST or None)
    if request.method == 'POST':
        if pay_form.is_valid():
            if request.POST.get('type') == 'VISA':
                addon = (total * 5) / 100
                total = total + addon
                order.paid = True
                order.save()
                messages.success(request, total)
                return redirect("/cash")
            back = int(request.POST.get('cash')) - total
            log = "Return" + " " + str(back)
            order.paid = True
            order.save()
            messages.success(request, log)
            return redirect("/cash")
    context = {'total': total,
               'table': table,
               'orders': orders,
               'order': order,
               'form': form}
    return render(request, template, context)


def new_order(request, pk):
    template = 'pos/new_order.html'
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            table_order = Order.objects.filter(table=pk)
            latest = table_order.latest('created')
            if latest.paid == True:
                order = Order()
            else:
                order = latest
            order.number = Order.objects.count() + 1
            order.table = Table.objects.get(number=pk)
            order.paid = False
            order.save()
            orderitem = OrderItem()
            product = form.cleaned_data.get('product')
            orderitem.product = Product.objects.get(title=product)
            orderitem.order = order
            orderitem.table = Table.objects.get(number=pk)
            orderitem.quantity = form.cleaned_data.get('quantity')
            orderitem.total_price = orderitem.quantity * orderitem.product.unit_price
            orderitem.discount = form.cleaned_data.get('discount')
            orderitem.notes = form.cleaned_data.get('notes')
            orderitem.save()
            return redirect('/table/' + pk)
    context = {'form': form}
    return render(request, template, context)


def shopping(request):
    template = 'pos/shopping.html'
    form = ShoppingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            item = Shopping()
            item.item = request.POST.get('item')
            item.quantity = request.POST.get('quantity')
            item.status = request.POST.get('status')
            item.Notes = request.POST.get('notes')
            item.save()
            messages.success(request, "Item has been added to shopping list")
            return redirect("/shopping")
    context = {'form': form}
    return render(request, template, context)
