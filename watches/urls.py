from django.conf.urls.static import static

from watches import settings
from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),

    path('admin/', admin.site.urls, name='admin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)