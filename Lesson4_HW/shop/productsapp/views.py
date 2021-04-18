from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import ProductModel


class ProductsList(ListView):
    model = ProductModel
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Просмотр товаров'
        return context


class ProductCreate(CreateView):
    model = ProductModel
    success_url = reverse_lazy('productsapp:product_review')
    fields = '__all__'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание товаров'
        return context
