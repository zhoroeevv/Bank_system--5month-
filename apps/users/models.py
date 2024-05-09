from typing import Iterable
from django.db import models
from django.utils.crypto import get_random_string

from django.contrib.auth.models import AbstractUser
from apps.users.validators import validate_phone_number
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        max_length  = 255,
        verbose_name = 'Номер телефона',
        validators=[validate_phone_number]
    )
    age = models.IntegerField(
        default=0,
        verbose_name='Возраст'
    )
    balance = models.IntegerField(
        default=0,
        verbose_name = 'Баланс',
        blank=True, null=True
    )
    wallet_address = models.CharField(
        max_length = 12,
        unique=True,blank=True,null=True,
        verbose_name = 'ID кошелька'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата регистрации'
    )

    def save(self, *args, **kwargs):
        if not self.wallet_address:
            unique_address_genereted = False
            while not unique_address_genereted:
                wallet_address = get_random_string(length=12)
                if not User.objects.filter(wallet_address=wallet_address).exists():
                    unique_address_genereted = True
            self.wallet_address = wallet_address
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.wallet_address} \n     username:{self.username}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'