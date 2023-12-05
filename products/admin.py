from django.contrib import admin

# Register your models here.
from .models import Product, models

admin.site.register(Product)






class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'is_available']
    search_fields = ['name', 'brand__name']
    list_filter = [ 'is_available']
    fields = ['name', 'description', 'price', 'stock_quantity', 'is_featured', 'is_available', 'rating', 'reviews_count', 'weight', 'dimensions', 'manufacturer', 'warranty', 'color', 'material', 'specifications']