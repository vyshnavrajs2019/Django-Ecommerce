from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from datetime import datetime

# Create your models here.
class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    added_on = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return f'Cart({self.product.name},{self.owner.username})'