from django.forms import ModelForm
from django import forms

from .models import Product, Order


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # instance = getattr(self,'instance',None)

        # widgets = {
        #      'name':  forms.TextInput(attrs = {'class':'form-control'}),
        #      'price': forms.NumberInput(attrs={'class': 'form-control'}),
        #      'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        #      'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
        # }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['total_quantity', 'grand_total', 'total_discount', 'status']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['total_quantity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Total Quantity'})
