from django.urls import path
from .views import register, home, products, add_view, delete_view, edit_view

app_name = 'seller'

urlpatterns = [
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('products/', products, name = 'products'),
    path('products/new', add_view, name = 'new-product'),
    path('products/<int:pid>/edit', edit_view, name = 'edit-product'),
    path('products/<int:pid>/delete', delete_view, name = 'delete-product'),
]
