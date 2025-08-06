from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('dresses', 'Dresses'),
        ('scarves', 'Scarves'),
        ('bags', 'Bags'),
        ('shirts', 'Shirts'),
        ('jeans', 'Jeans'),
        ('sweaters', 'Sweaters'),
        ('sleeves', 'Sleeves'),
        ('beanies', 'Beanies'),
        ('caps', 'Caps'),
        ('knitwear', 'Knitwear'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

