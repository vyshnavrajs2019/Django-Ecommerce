from django import forms
from .models import Seller, CheckSeller

class CheckSellerForm(forms.ModelForm):
    is_seller = forms.BooleanField(label = 'Are  you a seller ?', help_text = '', required = False)
    class Meta:
        model = CheckSeller
        fields = ('is_seller',)

class SellerForm(forms.ModelForm):

    company = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Company Name'}))
    location = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Location'}))
    zipcode = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Zipcode', 'maxlength': 6, 'minlength': 6}))
    mobile = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-input form-input-sm', 'placeholder': 'Mobile', 'maxlength': 10, 'minlength': 10}))

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(SellerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Seller
        fields = ('company','location','zipcode','mobile')

    def clean_mobile(self, *args, **kwargs):
        self.mobile = self.cleaned_data.get('mobile')
        if len(self.mobile) == 10:
            try:
                int(self.mobile)
            except Exception:
                raise forms.ValidationError("Mobile number must be valid.")
            return self.mobile
        else:
            raise forms.ValidationError("Mobile number must be 10 characters long.")

    def clean_zipcode(self, *args, **kwargs):
        self.zipcode = self.cleaned_data.get('zipcode')
        if len(self.zipcode) == 6:
            try:
                int(self.zipcode)
            except Exception:
                raise forms.ValidationError("Zipcode must be valid.")
            return self.zipcode
        else:
            raise forms.ValidationError("Zipcode must be 6 characters long.")