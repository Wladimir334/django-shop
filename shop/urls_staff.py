from django.urls import path

from tkinter.font import names

from .views import (CategoryCreateView, CategoryListView,
                    ProductListView, ProductCreateView, ProductDetailView)

app_name = 'staff'
urlpatterns = [
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/', CategoryListView.as_view(), name='categories'),

    path('products/add', ProductCreateView.as_view(), name='product_add'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='products'),
 ]