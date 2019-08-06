from django.db import models
from django.contrib.auth.models import User

class CheckSeller(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_seller = models.BooleanField(verbose_name = 'seller', default = False)
    

class Seller(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    company = models.CharField(max_length = 200, blank = False, null = False)
    location = models.CharField(max_length = 350, blank = False, null = False)
    zipcode = models.CharField(max_length = 6, blank = False, null = False)
    mobile = models.CharField(max_length = 10, blank = False, null = False)