# products/forms.py
from django import forms
from .models import Product, Category, Brand

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity', 'is_featured', 'is_available', 'rating', 'reviews_count', 'weight', 'dimensions', 'manufacturer', 'warranty', 'color', 'material', 'specifications']


