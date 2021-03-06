from django.conf.urls.static import static

from watches import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basketapp/', include('basketapp.urls', namespace='basketapp')),
    path('order/', include('orderapp.urls', namespace='orderapp')),
    path('my/admin/', include('adminapp.urls', namespace='my_admin')),
    path('', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls, name='admin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)