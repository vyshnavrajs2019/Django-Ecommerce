from django.db import models

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
    name = models.CharField(max_length = 300, blank = False, null = False)
    description = models.TextField(max_length = 1500, blank = False, null = False)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1, null = True, blank = True, default = 0)
    price = models.DecimalField(max_digits = 7, decimal_places = 2, blank = False, null = False)
    size = models.CharField(choices = SHIRT_SIZES + PANT_SIZES, max_length = 3, blank = False, null = False)
    color = models.CharField(max_length = 100, blank = False, null = False)
    material = models.CharField(max_length = 200, blank = False, null = False)
    dress_type = models.CharField(choices = DRESS_TYPE, max_length = 8, blank = False, null = False)
    quantity = models.IntegerField(blank = False, null = False)
    image = models.ImageField(upload_to = 'product-img', blank = False, null = False)