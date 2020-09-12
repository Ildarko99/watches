from django.shortcuts import render
import json


# Create your views here.
# root is "mainapp/templates/" folder
from mainapp.models import ProductCategory


def index(request):
    watches = [
        {
            "image": "/static/images/p-1.png",
            "name": "Casio",
            "shot_descr": "Casio watches",
            "price": "300$"

        },
        {
            "image": "/static/images/p-2.png",
            "name": "Candino",
            "shot_descr": "Candino watches",
            "price": "500$",

        },
        {
            "image": "/static/images/p-3.png",
            "name": "Patek",
            "shot_descr": "Patek watches",
            "price": "1000$",

        },
        {
            "image": "/static/images/p-4.png",
            "name": "Seiko",
            "shot_descr": "Seiko watches",
            "price": "450$",

        },
    ]

    context = {
        'page_title': 'Luxury watches | Home page',
        'breadcrumbs_active': 'Home',
        'watches': watches,
    }
    return render(request, 'mainapp/index.html', context)

def checkout(request):
    context = {
        'page_title': 'Luxury watches | Basket',
        'breadcrumbs_active': 'Basket'
    }
    return render(request, 'mainapp/checkout.html', context)

def products(request):
    categories = ProductCategory.objects.all()
    context = {
        'page_title': 'Luxury watches | Our watches',
        'breadcrumbs_active': 'Products',
        'categories': categories,
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {
        'page_title': 'Luxury watches | Contacts page',
        'breadcrumbs_active': 'Contacts'
    }
    return render(request, 'mainapp/contact.html', context)

def single(request):
    context = {
        'page_title': 'Luxury watches | Product page',
        'breadcrumbs_active': 'Product'
    }
    return render(request, 'mainapp/single.html', context)

def blog(request):
    context = {
        'page_title': 'Luxury watches | Our blog',
        'breadcrumbs_active': 'Blog'
    }
    return render(request, 'mainapp/typo.html', context)