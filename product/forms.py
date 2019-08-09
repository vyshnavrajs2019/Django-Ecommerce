from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'size',
            'color',
            'material',
            'dress_type',
            'quantity',
            'image'
        )

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = {
            'location'
        }