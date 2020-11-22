from mainapp.models import ProductCategory


def categories(request):     #show product categories menu
    categories = ProductCategory.objects.all()
    return {
        'categories': categories
    }