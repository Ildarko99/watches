from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from basketapp.models import BasketItem
from mainapp.models import Product


def index(request):
    context = {
        'page_title': 'Luxury watches | Basket',
        'breadcrumbs_active': 'Basket'
    }
    return render(request, 'basket/checkout.html', context)

def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = BasketItem(user=request.user, product=product)

    if not basket:
        basket = BasketItem(user=request.user, product=product) #not in db

    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))