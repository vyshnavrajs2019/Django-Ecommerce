from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input form-input-md', 'placeholder': 'Email'}))
    email.label_suffix = ""

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input form-input-md', 'placeholder': 'Username'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input form-input-md', 'placeholder': 'Password'}), label = 'Password')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input form-input-md', 'placeholder': 'Confirm-Password'}), label = 'Confirm-Password')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label_suffix = ""

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2'
        ]

    def clean_email(self):
        self.email = self.cleaned_data.get('email')
        if User.objects.filter(email = self.email).first():
            raise forms.ValidationError("This email has been taken. Try a different email.")
        else:
            return self.email