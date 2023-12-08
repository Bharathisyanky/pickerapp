
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, SubCategory
from .forms import CategoryForm, SubCategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'categories/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})

def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    return render(request, 'categories/subcategory_list.html', {'subcategories': subcategories})

def subcategory_detail(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    return render(request, 'categories/subcategory_detail.html', {'subcategory': subcategory})

def subcategory_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubCategoryForm()
    return render(request, 'categories/subcategory_form.html', {'form': form})

def subcategory_update(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubCategoryForm(instance=subcategory)
    return render(request, 'categories/subcategory_form.html', {'form': form})

def subcategory_delete(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('subcategory_list')
    return render(request, 'categories/subcategory_confirm_delete.html', {'subcategory': subcategory})