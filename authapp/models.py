from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст', default=18)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True

    def basket_cost(self):
        return sum(item.product.price * item.quantity for item in
                   self.user_basket.all())  # user_basket, потому что прописан RELATED_NAME в классе BasketItem,
        # иначе нужно писать basketitem_set.all()

    def basket_total_quantity(self):
        return sum(item.quantity for item in self.user_basket.all())

    # def delete_all(self):                         не работает TODO: починить это в корзине
    #     basket_items = self.user_basket.all()
    #     if basket_items:
    #         self.user_basket.all().delete()


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=128, blank=True)
    about_me = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)
    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()