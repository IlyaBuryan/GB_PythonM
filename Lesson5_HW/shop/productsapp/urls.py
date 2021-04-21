from django.urls import path

from .views import ProductsList, ProductCreate, save_good_form

app_name = 'productsapp'

urlpatterns = [
    path('', ProductsList.as_view(), name='product_review'),
    path('product-add/', ProductCreate, name='product_add'),
    path('good_create/', save_good_form, name='good_create'),
]
