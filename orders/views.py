from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Order, OrderItem


class OrderDetail(DetailView):
    model = Order
    template_name = 'orders/detail.html'
    context_object_name = 'order'

    def get_context_data(self, *args, **kwargs):
        table = self.kwargs['pk']
        context = super(OrderDetail, self).get_context_data(*args, **kwargs)
        context['orderitem'] = OrderItem.objects.filter(order=table)
        context['table'] = table
        return context


class OrderList(ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'
    paginate_by = 10
