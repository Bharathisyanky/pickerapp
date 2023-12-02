# products/forms.py
from django import forms
from .models import Product, Category, Brand

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity', 'category', 'brand', 'is_featured', 'is_available', 'rating', 'reviews_count', 'weight', 'dimensions', 'manufacturer', 'warranty', 'color', 'material', 'specifications', 'featured_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['brand'].queryset = Brand.objects.all()
