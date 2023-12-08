
from django.urls import path
from .views import category_list, category_detail, category_create, category_update, category_delete, subcategory_list, subcategory_detail, subcategory_create, subcategory_update, subcategory_delete

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/', category_detail, name='category_detail'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:category_id>/update/', category_update, name='category_update'),
    path('categories/<int:category_id>/delete/', category_delete, name='category_delete'),
    path('subcategories/', subcategory_list, name='subcategory_list'),
    path('subcategories/<int:subcategory_id>/', subcategory_detail, name='subcategory_detail'),
    path('subcategories/create/', subcategory_create, name='subcategory_create'),
    path('subcategories/<int:subcategory_id>/update/', subcategory_update, name='subcategory_update'),
    path('subcategories/<int:subcategory_id>/delete/', subcategory_delete, name='subcategory_delete'),
]