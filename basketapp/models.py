from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils.functional import cached_property

from authapp.models import ShopUser
from mainapp.models import Product

class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class   BasketItem(models.Model):
    # user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_basket',
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)
    @staticmethod
    def get_items(user):
        return BasketItem.objects.filter(user=user).order_by('product__category')