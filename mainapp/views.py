from django.conf import settings
from mainapp.models import Product, ProductCategory
from django.shortcuts import render


def index(request):
    products_list = Product.objects.all()[:4]
    print(products_list.query)

    context = {
        'title': 'мой магазин',
        'products': products_list
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    links_menu = ProductCategory.objects.all()
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/contact.html', context)
