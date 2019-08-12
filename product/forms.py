from django import forms
from .models import Product, Order, SHIRT_SIZES, PANT_SIZES, DRESS_TYPE

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Name'}))
    description = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-input form-input-md', 'placeholder': 'Description'}))
    price = forms.DecimalField(widget = forms.NumberInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Price', 'step': 0.01}))
    size = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Size'}), choices=SHIRT_SIZES+PANT_SIZES)
    color = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Color'}))
    material = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Material'}))
    dress_type = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Dress Type'}), choices=DRESS_TYPE)
    quantity = forms.DecimalField(widget = forms.NumberInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Quantity', 'step': 1}))
    image = forms.FileField(widget = forms.FileInput(attrs={'class': 'btn btn-sm', 'placeholder': 'Image'}))

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

    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input form-input-sm mb-1', 'placeholder': 'Address, state, zipcode'}))

    class Meta:
        model = Order
        fields = {
            'location'
        }