import json
import os

from django.shortcuts import render

# Create your views here.
MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'products/index.html', context)

def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geekshop - каталог',
        'categories': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'products': json.load(open(file_path, encoding='utf-8'))
    }

    return render(request, 'products/products.html', context)