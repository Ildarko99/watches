from django.urls import path, re_path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='basket'),
    path('add/product/<int:pk>/', basketapp.add, name='add'),
    # re_path('^add/product/(?P<pk>\d+)/$', basketapp.add, name='add'),
]
