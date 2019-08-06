from django import forms
from .models import Product

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