from django.conf.urls import url

from views import TableList

urlpatterns = [
    url('^$', TableList.as_view(), name="table_list"),
]
