from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils.functional import cached_property

from authapp.models import ShopUser
from mainapp.models import Product


class BasketItem(models.Model):
    # user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_basket',
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    add_datetime = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_items(user):
        return BasketItem.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_product(user, product):
        return BasketItem.objects.filter(user=user, product=product).first()

    @staticmethod
    def get_item(pk):
        return BasketItem.objects.get(pk=pk)

    @classmethod
    def get_products_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]

    # def save(self, *args, **kwargs):
    #     self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(BasketItem, self).save(*args, **kwargs)


