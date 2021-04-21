from .models import ProductModel
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
