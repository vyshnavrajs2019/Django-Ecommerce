from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from .views import home, register, cart, login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(next_page = 'home'), name = 'logout'),
    path('cart/', cart, name = 'cart'),
    path('company/', include('sellers.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)