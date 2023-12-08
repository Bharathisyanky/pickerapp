from django import forms
from .models import Category, SubCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SubCategoryForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = SubCategory
        fields = ['name', 'categories', 'description']