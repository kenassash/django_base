from django.shortcuts import render


def index(request):
    context = {
        'custom_users': [
            {
                'name': 'Oleg Maslov'
            },
            {
                'name': 'Ivan Petrov'
            }
        ],
        'title': 'мой магазин'
    }
    return render(request, 'mainapp/index.html', context)


links_menu = [
    {'href': 'products', 'name': 'Все'},
    {'href': 'products_home', 'name': 'Дом'},
    {'href': 'products_modern', 'name': 'Модерн'},
    {'href': 'products_office', 'name': 'Офис'},
    {'href': 'products_classic', 'name': 'Классика'},
]


def products(request):
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/products.html', context)


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/products.html', context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/products.html', context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/products.html', context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'links_menu': links_menu,
        'title': "Товары"
    }
    return render(request, 'mainapp/products.html', context)
