from django.conf.urls import url

from views import ProductList, ShoppingList, CategoryList

urlpatterns = [
    url(r'^$', ProductList.as_view()),
    url(r'^shopping/', ShoppingList.as_view()),
    url(r'^category/', CategoryList.as_view()),
]
