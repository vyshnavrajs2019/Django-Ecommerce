from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SellerForm
from .decorators import is_seller, company_already_registered
from product.forms import ProductForm
from product.models import Product
from django.conf import settings
from django.conf.urls.static import static

@login_required
@is_seller
def register_company(request, *args, **kwargs):
    user = request.user
    if len(user.seller_set.all()):
        return redirect('seller:home')
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.owner = request.user
            form.save()
            return redirect('seller:home')
    else:
        form = SellerForm()
    return render(request, 'sellers/register.html',{
        'form': form
    })

@login_required
@is_seller
@company_already_registered
def company_home(request, *args, **kwargs):
    return render(request, 'sellers/home.html')

@login_required
@is_seller
@company_already_registered
def company_products(request, *args, **kwargs):
    try:
        products = request.user.seller_set.all().first().product_set.all()
    except Exception:
        products = []

    return render(request, 'sellers/products.html', {
        'products': products
    })

@login_required
@is_seller
@company_already_registered
def company_add_product(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProductForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.company = request.user.seller_set.all().first()
            form.save()
            return redirect('seller:products')
    else:
        form = ProductForm()
    return render(request, 'sellers/add_product.html', {
        'form': form
    })

@login_required
@is_seller
@company_already_registered
def company_delete_product(request, *args, **kwargs):
    pid = kwargs.get('pid')
    if request.method == 'GET':
        user = request.user
        pdt = Product.objects.get(pk=pid)
        pdt.delete()
        return redirect('seller:products')