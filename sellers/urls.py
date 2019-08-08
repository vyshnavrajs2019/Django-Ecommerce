from django.urls import path
from .views import register_company, company_home, company_products, company_add_product, company_delete_product

app_name = 'seller'

urlpatterns = [
    path('register/', register_company, name = 'register'),
    path('', company_home, name = 'home'),
    path('products/', company_products, name = 'products'),
    path('products/new', company_add_product, name = 'new-product'),
    path('products/<int:pid>/delete', company_delete_product, name = 'delete-product')
]
