from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from basketapp.models import BasketItem
from mainapp.models import Product


@login_required
def index(request):
    # basket_items = BasketItem.objects.filter(user=request.user)
    basket_items = request.user.basketitem_set.all()
    basket_cost = sum(item.product.price * item.quantity for item in basket_items)
    context = {
        'page_title': 'Luxury watches | Basket',
        'breadcrumbs_active': 'Basket',
        'basket_items': basket_items,
        'basket_cost': basket_cost,
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
    return HttpResponseRedirect(reverse('basketapp:basketapp'))
