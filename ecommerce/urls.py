from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path
from .views import home, register, cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', auth_view.LoginView.as_view(template_name = 'auth/login.html'), name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(next_page = 'home'), name = 'logout'),
    path('cart/', cart, name = 'cart')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
