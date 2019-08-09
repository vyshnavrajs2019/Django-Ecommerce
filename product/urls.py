from django.urls import path
from .views import detail_view, buy_view

app_name = 'product'

urlpatterns = [
    path('<int:id>', detail_view, name = 'detail'),
    path('<int:id>/buy', buy_view, name = 'buy')
]