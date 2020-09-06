from django.shortcuts import render


# Create your views here.
# root is "mainapp/templates/" folder

def index(request):
    return render(request, 'mainapp/index.html')

def checkout(request):
    return render(request, 'mainapp/checkout.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def products(request):
    return render(request, 'mainapp/products.html')

def single(request):
    return render(request, 'mainapp/single.html')

def blog(request):
    return render(request, 'mainapp/typo.html')