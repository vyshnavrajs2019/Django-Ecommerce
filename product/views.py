from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
# Create your views here.

def detail_view(request, id):
    pdt = Product.objects.filter(id = id).first()
    if not pdt:
        return redirect('home')
    return render(request, 'product/detail.html', {
        'product': pdt
    })

@login_required
def buy_view(request, id):
    pdt = Product.objects.filter(pk = id).first()
    if not pdt:
        return redirect('home')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.customer = request.user
            if pdt.quantity <= 0:
                messages.error(request, f'Product, {pdt.name}, is not in stock.')
                return redirect('product:detail', id=id)
            pdt.quantity -= 1
            pdt.save()
            form.product = pdt
            form.seller = pdt.company
            form.save()
            messages.success(request, f'Your order for the product {pdt.name} was successfull.')
            return redirect('product:detail', id=id)
    else:
        form = OrderForm()
    return render(request, 'product/buy.html',{
            'form': form
        })