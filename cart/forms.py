from django.forms import ModelForm
from .models import Product,Order


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('total_quantity', 'grand_total', 'total_discount', 'status', 'product')
