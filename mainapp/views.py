import random

from django.shortcuts import render, get_object_or_404
import json

# Create your views here.
# root is "mainapp/templates/" folder
from django.urls import ResolverMatch

from mainapp.models import ProductCategory, Product


def get_menu():
    test = ProductCategory.objects.all()
    print(type(test))
    print(test)
    return ProductCategory.objects.all()


# возвращает лист рандомных продуктов из каталога, исп-я на Главной
def random_products(request):
    products_ids_list = Product.objects.values_list('id', flat=True)
    random_products_ids_list = []
    random_products_list = []
    qty = 4 if request.resolver_match.url_name == 'index' else 6
    while len(random_products_ids_list)<qty:
        random_product_id = random.choice(products_ids_list)
        if random_product_id not in random_products_ids_list:
            random_products_ids_list.append(random_product_id)
    for i in random_products_ids_list:
        random_products_list.append(Product.objects.get(pk=i))
    # print(type(random_products_list))
    # print(random_products_list)
    # print(random_products_list[0].pk)
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
        'random_products': random_products(request),
    }
    return render(request, 'mainapp/products.html', context)

def product_page(request, pk):
    context = {
        'page_title': 'Luxury watches | Product page',
        'breadcrumbs_active': 'Products / Product page',  #нужно доделать динамику
        'categories': get_menu(),
        'product': get_object_or_404(Product, pk=pk),
    }
    return render(request, 'mainapp/single.html', context)


def catalog(request, pk):       #генерит меню каталога -> ссылки на категории
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
        'breadcrumbs_active': 'Products / Product page',
    }
    return render(request, 'mainapp/single.html', context)


def blog(request):
    context = {
        'page_title': 'Luxury watches | Our blog',
        'breadcrumbs_active': 'Blog',

    }
    return render(request, 'mainapp/typo.html', context)
