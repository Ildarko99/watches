from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from basketapp.models import BasketItem
from mainapp.models import Product


@login_required
def index(request):
    # basket_items = BasketItem.objects.filter(user=request.user)
    basket_items = request.user.user_basket.all()

    context = {
        'page_title': 'Luxury watches | Basket',
        'breadcrumbs_active': 'Basket',
        'basket_items': basket_items,

    }
    return render(request, 'basketapp/checkout.html', context)


@login_required
def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = BasketItem(user=request.user, product=product)

    if not basket:
        basket = BasketItem(user=request.user, product=product)  # not in db

    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete(request, pk):
    basket = get_object_or_404(BasketItem, pk=pk).delete()
    basket_items = request.user.user_basket.all()
    return HttpResponseRedirect(reverse('basketapp:basketapp'))

@login_required
def delete_all(request):
    basket_items = BasketItem.objects.filter(user=request.user)
    if basket_items:
        BasketItem.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
