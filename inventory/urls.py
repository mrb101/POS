from django.conf.urls import url

from views import ShoppingList, CategoryDetail, CategoryList

urlpatterns = [
    url(r'^shopping/$', ShoppingList.as_view(), name="Shopping_list"),
    url(r'^$', CategoryList.as_view(), name="category_list"),
    url(r'^(?P<slug>[-\w]+)/', CategoryDetail.as_view(), name="category_detail"),
]
