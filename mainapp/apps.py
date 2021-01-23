from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = 'mainapp'

    def ready(self):
        from mainapp.models import ProductCategory, Product