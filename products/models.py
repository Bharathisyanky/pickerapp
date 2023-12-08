
from django.db import models
from django.utils import timezone
from categories.models import SubCategory

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    reviews_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Additional fields for a more comprehensive product model
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    warranty = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)
    specifications = models.TextField(null=True, blank=True)
    #featured_image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)
    location_code_prefix = models.CharField(max_length=10, unique=True)
    # Add other fields related to the store

    def __str__(self):
        return self.name
    
