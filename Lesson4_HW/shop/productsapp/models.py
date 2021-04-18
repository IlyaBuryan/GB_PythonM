from django.db import models

class ProductModel(models.Model):
    MEASURES_FIELDS = [
        ('KG', 'Kilograms'),
        ('UN', 'Units'),
    ]

    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    measure = models.CharField(choices=MEASURES_FIELDS, max_length=2)
    vendor = models.CharField(max_length=150)

    def __str__(self):
        return self.name
