from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SellerForm
from .decorators import is_seller, company_already_registered

@login_required
@is_seller
def register_company(request):
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
def company_home(request):
    return render(request, 'sellers/home.html')

@login_required
@is_seller
@company_already_registered
def company_products(request):
    return render(request, 'sellers/products.html')

@login_required
@is_seller
@company_already_registered
def company_add_product(request):
    return render(request, 'sellers/add_product.html')