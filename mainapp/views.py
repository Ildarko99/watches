from django.shortcuts import render


# Create your views here.
# root is "mainapp/templates/" folder

def index(request):
    context = {
        'page_title': 'Luxury watches | Home page',
        'breadcrumbs_active': 'Home'
    }
    return render(request, 'mainapp/index.html', context)

def checkout(request):
    context = {
        'page_title': 'Luxury watches | Basket',
        'breadcrumbs_active': 'Basket'
    }
    return render(request, 'mainapp/checkout.html', context)

def contact(request):
    context = {
        'page_title': 'Luxury watches | Contacts page',
        'breadcrumbs_active': 'Contacts'
    }
    return render(request, 'mainapp/contact.html', context)

def products(request):
    context = {
        'page_title': 'Luxury watches | Our watches',
        'breadcrumbs_active': 'Products'
    }
    return render(request, 'mainapp/products.html', context)

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