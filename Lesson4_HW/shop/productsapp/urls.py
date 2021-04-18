from django.urls import path

from .views import ProductsList, ProductCreate

app_name = 'productsapp'

urlpatterns = [
    path('', ProductsList.as_view(), name='product_review'),
    path('product-add/', ProductCreate.as_view(), name='product_add'),
]
