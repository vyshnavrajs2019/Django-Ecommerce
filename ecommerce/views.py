from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from sellers.forms import CheckSellerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from product.models import Product, Order
from user.models import Cart

def login_view(request, *args, **kwargs):
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

def register(request, *args, **kwargs):
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

def home(request, *args, **kwargs):
    pdts = Product.objects.filter(rating__gte = 0)
    pdts_ = []
    for pdt in pdts:
        obj = {'product': pdt, 'in_cart': False}
        if request.user.is_authenticated:
            if Cart.objects.filter(owner = request.user, product = pdt).first():
                obj['in_cart'] = True
        pdts_.append(obj)
    return render(request, 'search.html', {
        'products': pdts_
    })

def search(request, *args, **kwargs):
    if request.method == 'GET':
        try:
            query = request.GET.get('query')
            min_price = int(request.GET.get('min_price') or 100)
            max_price = int(request.GET.get('max_price') or 2000)
            sort_by = request.GET.get('sort_by') or 'price-low-to-high'
            # check query string
            if not query:
                raise Exception
            if min_price > max_price:
                raise Exception
            if sort_by not in ['price-low-to-high', 'price-high-to-low']:
                raise Exception
            print(query, min_price, max_price, sort_by)
            # get the data
            q1 = Q(name__icontains = query)
            q2 = Q(description__icontains = query)
            q3 = Q(material__icontains = query)
            q4 = Q(price__gte = min_price)
            q5 = Q(price__lte = max_price)

            if sort_by == 'price-low-to-high':
                sort_by = 'price'
            else:
                sort_by = '-price'

            products = Product.objects.filter(
                (q1 | q2 | q3) & q4 & q5 
            ).order_by(sort_by).order_by('-rating')

            print(products)

            pdts_ = []
            for pdt in products:
                obj = {'product': pdt, 'in_cart': False}
                if request.user.is_authenticated:
                    if Cart.objects.filter(owner = request.user, product = pdt).first():
                        obj['in_cart'] = True
                pdts_.append(obj)
            return render(request, 'search.html', {
                'products': pdts_,
                'query': query,
                'min_price': min_price,
                'max_price': max_price,
                'sort_by': sort_by
            })

        except Exception:
            return redirect('home')

@login_required
def cart(request, *args, **kwargs):
    cart_items = Cart.objects.filter(owner = request.user)
    return render(request, 'cart.html', {
        'cart_items': cart_items
    })

@login_required
def add_cart(request, *args, **kwargs):
    pid = kwargs.get('id')
    pdt = Product.objects.filter(pk = pid).first()
    next_url = request.GET.get('next')
    if pdt:
        if Cart.objects.filter(owner = request.user, product = pdt).first():
            return redirect(next_url or 'home')
        cart = Cart(owner = request.user, product = pdt)
        cart.save()
    return redirect(next_url or 'home')

@login_required
def rem_cart(request, *args, **kwargs):
    pid = kwargs.get('id')
    pdt = Product.objects.filter(pk = pid).first()
    next_url = request.GET.get('next')
    if pdt:
        cart = Cart.objects.filter(owner = request.user, product = pdt).first()
        if cart:
            cart.delete()
    return redirect(next_url or 'home')

@login_required
def order(request):
    orders = Order.objects.filter(customer = request.user)
    return render(request, 'orders.html', {
        'orders': orders
    })

@login_required
def delete_order(request, id):
    order = Order.objects.filter(id = id).first()

    if order and order.customer == request.user and not order.is_placed:
        order.delete()
        messages.success(request, f'You have canceled ordering {order.product.name}')
        return redirect('order')
    else:
        messages.error(request, f'You tried to cancel an order that is either placed or you not ordered.')
        return redirect('home')