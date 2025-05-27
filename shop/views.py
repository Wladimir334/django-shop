from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)

from .forms import CategoryCreateForm, ProductCreateForm
from .models import Category, Product


##############################   АДМИНКА    ###############################

# класс для создания новой категории
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'admin_pages/add_category.html'
    success_url = reverse_lazy('staff:categories')


# Класс для просмотрв категорий
class CategoryListView(ListView):
    model = Category
    template_name = 'admin_pages/list_category.html'
    context_object_name = 'categories'

# класс для создания товара
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'admin_pages/add_product.html'
    success_url = reverse_lazy('staff:products')

# класс для обображения товара
class ProductListView(ListView):
    model = Product
    template_name = 'admin_pages/list_product.html'
    context_object_name = 'products'

# Класс для отображения информации о товаре
class ProductDetailView(DetailView):
    model = Product
    template_name = 'admin_pages/detail_product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

def index(request):
    context = {"title": "Главная страница"}
    return render(request, template_name='shop/index.html', context=context)