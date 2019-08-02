from django import forms
from .models import Seller, CheckSeller

class CheckSellerForm(forms.ModelForm):
    is_seller = forms.BooleanField(label = 'Are  you a seller ?', help_text = '', required = False)
    class Meta:
        model = CheckSeller
        fields = ('is_seller',)

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('company','location','zipcode','mobile')