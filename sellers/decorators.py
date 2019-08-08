from django.shortcuts import redirect
from functools import wraps

def is_seller(func):
    @wraps(func)
    def decor(request, *args, **kwargs):
        user = request.user
        try:
            if user.checkseller.is_seller:
                return func(request, *args, **kwargs)
            return redirect('home')
        except Exception:
            return redirect('home')
    return decor

def company_already_registered(func):
    @wraps(func)
    def decor(request, *args, **kwargs):
        user = request.user
        if len(user.seller_set.all()) == 0:
            return redirect('seller:register')
        return func(request, *args, **kwargs)
    return decor
