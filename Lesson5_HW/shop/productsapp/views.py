from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView

from .forms import ProductForm
from .models import ProductModel


class ProductsList(ListView):
    model = ProductModel
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Просмотр товаров'
        return context


def ProductCreate(request):
    data = dict()
    form = ProductForm()
    context = {'form': form}
    data['html_form'] = render_to_string('productsapp/productmodel_form.html', context, request=request)
    return JsonResponse(data)


def save_good_form(request):
    data = dict()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            object_list = ProductModel.objects.all()
            data['html_good_list'] = render_to_string('productsapp/goods_list.html', {
                'object_list': object_list
            })
    return JsonResponse(data)
