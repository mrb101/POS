"""eco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from pos import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^orders/', include('orders.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^$', views.index, name='home'),
    url(r'^login', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^cash/', views.cash, name='cash'),
    url(r'^table/(?P<pk>\d+)/$', views.table, name='table'),
    url(r'^table/(?P<pk>\d+)/(?P<pk2>\d+)/$', views.table, name='table'),
    url(r'^checkout/(?P<pk>\d+)/$', views.checkout, name='checkout'),
    url(r'^kitchen/', views.kitchen, name='kitchen'),
    url(r'^bar/', views.bar, name='bar'),
    url(r'^menu/', views.menu, name='menu'),
    url(r'^table/(?P<pk>\d+)/new', views.new_order, name='new_order'),
    url(r'^table/(?P<pk>\d+)/checkout', views.checkout, name='checkout'),
    url(r'^shopping/', views.shopping, name='shopping'),
]
