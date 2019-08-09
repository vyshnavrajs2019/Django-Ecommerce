from django.db import models
from sellers.models import Seller
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime

# shirts / tshirts
SHIRT_SIZES = [
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('vl', 'VL'),
    ('xl', 'XL')
]

# pants / trousers
PANT_SIZES = [
    (str(i),i) for i in range(26,43)
]

# dress type
DRESS_TYPE = [
    ('shirt', 'Shirt'),
    ('t-shirt', 'T-Shirt'),
    ('pants', 'Pants'),
    ('trousers', 'Trousers')
]

class Product(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField(max_length = 1500)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1, null = True, blank = True, default = 0)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    size = models.CharField(choices = SHIRT_SIZES + PANT_SIZES, max_length = 3)
    color = models.CharField(max_length = 100)
    material = models.CharField(max_length = 200)
    dress_type = models.CharField(choices = DRESS_TYPE, max_length = 8)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to = 'product-img')
    company = models.ForeignKey(Seller, on_delete = models.CASCADE)

    def get_buy_url(self):
        return reverse('product:buy', kwargs = {'id': self.id})

    def get_pdt_url(self):
        return reverse('product:detail', kwargs = {'id': self.id})

    def get_del_url(self):
        return reverse('seller:delete-product', kwargs={'pid':self.id})

    def get_edit_url(self):
        return reverse('seller:edit-product', kwargs = {'pid': self.id})

    def get_add_cart_url(self):
        return reverse('cart-add', kwargs = {'id': self.id})

    def get_rem_cart_url(self):
        return reverse('cart-remove', kwargs = {'id': self.id})

    def __str__(self):
        return f'{self.name}, {self.size}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    location = models.CharField(max_length = 250)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    ordered_on = models.DateTimeField(default = datetime.now)
    is_placed = models.BooleanField(default = False)

    def get_place_url(self):
        return reverse('seller:place-order', kwargs = {'id': self.id})

    def get_del_url(self):
        return reverse('order-remove', kwargs = {'id': self.id})

    def __str__(self):
        return f'Order({self.id})'