import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
import json

# Create your views here.
# root is "mainapp/templates/" folder
from django.urls import ResolverMatch

from mainapp.models import ProductCategory, Product


# def get_menu():   #ушло в контекстный процессор context_processors.py
#     return ProductCategory.objects.all()


# возвращает лист рандомных продуктов из каталога, исп-я на Главной и в каталоге
def random_products(request):
    products_ids_list = Product.objects.values_list('id', flat=True)
    random_products_ids_list = []
    random_products_list = []
    qty = 4 if request.resolver_match.url_name == 'index' else 6 #4 для Главной, 6 для страницы products
    while len(random_products_ids_list) < qty:
        random_product_id = random.choice(products_ids_list)
        if random_product_id not in random_products_ids_list:
            random_products_ids_list.append(random_product_id)
    for i in random_products_ids_list:
        random_products_list.append(Product.objects.get(pk=i))

    return random_products_list


def index(request):

    context = {
        'page_title': 'Luxury watches | Home page',
        'breadcrumbs_active': 'Home',
        'random_products': random_products(request),

    }
    return render(request, 'mainapp/index.html', context)


def products(request, page=1):
    # categories = ProductCategory.objects.all()

    products = random_products(request)
    products_paginator = Paginator(products, 3)
    try:
        products = products_paginator.page(page)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        'page_title': 'Luxury watches | Our watches',
        'breadcrumbs_active': 'Products',
        # 'categories': get_menu(), #ушло в контекстный процессор context_processors.py
        'random_products': products,
    }
    return render(request, 'mainapp/products.html', context)

def product_page(request, pk):

    # category = get_object_or_404(ProductCategory, pk=pk)

    context = {
        'page_title': 'Luxury watches | Product page',
        'breadcrumbs_active': 'Products / Product page',  #нужно доделать динамику
        # 'categories': get_menu(), #ушло в контекстный процессор context_processors.py
        'product': get_object_or_404(Product, pk=pk),
    }
    return render(request, 'mainapp/single.html', context)


def catalog(request, pk, page=1):       #генерит меню каталога -> ссылки на категории
    # try...
    #   category = ProductCategory.objects.get(pk=pk)
    # except...

    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category)

    products_paginator = Paginator(products, 3)
    try:
        products = products_paginator.page(page)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)


    context = {
        'page_title': 'Luxury watches | Products',
        # 'categories': get_menu(), #ушло в контекстный процессор context_processors.py
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


def single(request): #уже не исп-я TODO на карточке товара убрать харкодные товары и выключить и убрать из urls
    context = {
        'page_title': 'Luxury watches | Product page',
        'breadcrumbs_active': 'Products / Product page',
    }
    return render(request, 'mainapp/single.html', context)


def blog(request):
    context = {
        'page_title': 'Luxury watches | Our blog',
        'breadcrumbs_active': 'Blog',

    }
    return render(request, 'mainapp/typo.html', context)
