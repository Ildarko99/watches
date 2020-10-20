from django.urls import path, re_path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='basketapp'),
    path('add/product/<int:pk>/', basketapp.add, name='add'),

    path('change/<int:pk>/quantity/<int:quantity>/', basketapp.change),

    path('delete/basket/item/<int:pk>/', basketapp.delete, name='delete'),
    path('delete/basket/item/all/', basketapp.delete_all, name='delete_all'),
    # re_path('^add/product/(?P<pk>\d+)/$', basketapp.add, name='add'),
]
