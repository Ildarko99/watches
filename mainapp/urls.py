"""watches URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import mainapp.views as mainapp
import basketapp.views as basketapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('contact/', mainapp.contact, name='contact'),
    path('products/', mainapp.products, name='products'),

    path('category/<int:pk>/products/', mainapp.catalog, name='catalog'),
    path('products/<int:pk>/', mainapp.product_page, name='product_page'),
    # re_path(r'^category/(?P<pk>\d+)/products/$', mainapp.catalog, name='catalog'), как вариант через регулярки

    path('single/', mainapp.single, name='single'),
    path('blog/', mainapp.blog, name='blog'),
]
