from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    def basket_cost(self):
        return sum(item.product.price * item.quantity for item in self.user_basket.all())

    # def delete_all(self):                         не работает
    #     basket_items = self.user_basket.all()
    #     if basket_items:
    #         self.user_basket.all().delete()