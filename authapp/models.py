from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True

    def basket_cost(self):
        return sum(item.product.price * item.quantity for item in self.user_basket.all()) #user_basket, потому что прописан RELATED_NAME в классе BasketItem,
                                                                                            # иначе нужно писать basketitem_set.all()

    def basket_total_quantity(self):
        return sum(item.quantity for item in self.user_basket.all())


    # def delete_all(self):                         не работает
    #     basket_items = self.user_basket.all()
    #     if basket_items:
    #         self.user_basket.all().delete()