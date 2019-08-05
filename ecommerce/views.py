from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from sellers.forms import CheckSellerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.GET.get('next',None) != None:
                return redirect(request.GET.get('next'))
            try:
                if user.checkseller.is_seller:
                    return redirect('seller:home')
            except Exception:
                pass
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html',{
        'form': form
    })

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        is_seller_form = CheckSellerForm(request.POST)
        if form.is_valid() and is_seller_form.is_valid():
            user = form.save()
            is_seller_form_inst = is_seller_form.save(commit = False)
            is_seller_form_inst.user = user
            is_seller_form_inst.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account created for {username}')
            new_user = authenticate(username = username, password = password)
            login(request, new_user)
            return redirect('seller:register')
    else:
        form = UserRegistrationForm()
        is_seller_form = CheckSellerForm(request.POST)
    return render(request, 'auth/register.html',{
        'form': form,
        'is_seller_form': is_seller_form
    })

def home(request):
    return render(request, 'search.html')

@login_required
def cart(request):
    return render(request, 'cart.html')