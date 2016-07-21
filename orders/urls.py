from django.conf.urls import url

from views import OrderDetail, OrderList

urlpatterns = [
    url(r'^$', OrderList.as_view()),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view()),
]
