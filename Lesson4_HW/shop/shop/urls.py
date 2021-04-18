from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('productsapp.urls', namespace='productsapp')),
    path('admin/', admin.site.urls),
]
