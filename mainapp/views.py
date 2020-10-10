import random

from django.shortcuts import render, get_object_or_404
import json

# Create your views here.
# root is "mainapp/templates/" folder
from mainapp.models import ProductCategory, Product


def get_menu():
    return ProductCategory.objects.all()


# возвращает лист рандомных продуктов из каталога, исп-я на Главной
def random_products(request):
    products_ids_list = Product.objects.values_list('id', flat=True)
    random_products_ids_list = []
    random_products_list = []
    while len(random_products_ids_list)<4:
        random_product_id = random.choice(products_ids_list)
        if random_product_id not in random_products_ids_list:
            random_products_ids_list.append(random_product_id)
    for i in random_products_ids_list:
        random_products_list.append(Product.objects.get(pk=i))
    print(random_products_list)
    return random_products_list


def index(request):

    context = {
        'page_title': 'Luxury watches | Home page',
        'breadcrumbs_active': 'Home',
        'random_products': random_products(request),
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # categories = ProductCategory.objects.all()
    context = {
        'page_title': 'Luxury watches | Our watches',
        'breadcrumbs_active': 'Products',
        'categories': get_menu(),
    }
    return render(request, 'mainapp/products.html', context)


def catalog(request, pk):
    # try...
    #   category = ProductCategory.objects.get(pk=pk)
    # except...

    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category)
    context = {
        'page_title': 'Luxury watches | Products',
        'categories': get_menu(),
        'category': category,
        'products': products,
    }
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    context = {
        'page_title': 'Luxury watches | Contacts page',
        'breadcrumbs_active': 'Contacts',
    }
    return render(request, 'mainapp/contact.html', context)


def single(request):
    context = {
        'page_title': 'Luxury watches | Product page',
        'breadcrumbs_active': 'Product',
    }
    return render(request, 'mainapp/single.html', context)


def blog(request):
    context = {
        'page_title': 'Luxury watches | Our blog',
        'breadcrumbs_active': 'Blog',

    }
    return render(request, 'mainapp/typo.html', context)
