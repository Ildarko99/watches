from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'Luxury watches | Basket',
        'breadcrumbs_active': 'Basket'
    }
    return render(request, 'basket/checkout.html', context)