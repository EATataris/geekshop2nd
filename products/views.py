from django.shortcuts import render
from products.models import Product, ProductCategory
# Create your views here.


def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Geekshop - каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }

    return render(request, 'products/products.html', context)