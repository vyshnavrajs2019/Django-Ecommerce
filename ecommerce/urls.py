from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path
from .views import home, register, cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', auth_view.LoginView.as_view(template_name = 'auth/login.html'), name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'auth/logout.html'), name = 'logout'),
    path('cart/', cart, name = 'cart')
]
