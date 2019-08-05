from django import forms
from .models import Seller, CheckSeller

class CheckSellerForm(forms.ModelForm):
    is_seller = forms.BooleanField(label = 'Are  you a seller ?', help_text = '', required = False)
    class Meta:
        model = CheckSeller
        fields = ('is_seller',)

class SellerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(SellerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Seller
        fields = ('company','location','zipcode','mobile')