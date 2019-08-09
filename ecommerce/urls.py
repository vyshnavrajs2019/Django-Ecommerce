from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from .views import home, register, cart, login_view, add_cart, rem_cart, order, delete_order
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(next_page = 'home'), name = 'logout'),
    path('cart/', cart, name = 'cart'),
    path('company/', include('sellers.urls')),
    path('cart/<int:id>/add', add_cart, name = 'cart-add'),
    path('cart/<int:id>/delete', rem_cart, name = 'cart-remove'),
    path('product/', include('product.urls')),
    path('order/', order, name = 'order'),
    path('order/<int:id>/delete', delete_order, name = 'order-remove')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)