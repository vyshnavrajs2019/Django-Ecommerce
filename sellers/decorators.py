from django.shortcuts import redirect

def is_seller(func):
    def decor(request, *args, **kwargs):
        user = request.user
        try:
            if user.checkseller.is_seller:
                return func(request)
            else:
                return redirect('home')
        except:
            return redirect('home')
        
    return decor