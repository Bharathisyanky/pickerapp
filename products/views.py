from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Category, Brand
from django.db.models import Q
from .forms import ProductForm



# Create your views here.

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def update_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('new_quantity'))
        product.stock_quantity = new_quantity
        product.save()
        return JsonResponse({'message': 'Stock quantity updated successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def mark_out_of_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.is_available = False
        product.save()
        return JsonResponse({'message': 'Product marked as out of stock'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def products_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/products_by_category.html', {'category': category, 'products': products})

def products_by_brand(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    products = Product.objects.filter(brand=brand)
    return render(request, 'products/products_by_brand.html', {'brand': brand, 'products': products})

def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'products/search_products.html', {'products': products, 'query': query})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})