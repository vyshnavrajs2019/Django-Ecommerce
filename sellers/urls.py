from django.urls import path
from .views import register_company, company_home

app_name = 'seller'

urlpatterns = [
    path('register/', register_company, name = 'register'),
    path('', company_home, name = 'home')
]
