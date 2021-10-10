from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Baskets
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


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Baskets.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Baskets.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))