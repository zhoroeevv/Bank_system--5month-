from django.db import models
from django.contrib.auth import get_user_model

from apps.users.models import User

# Create your models here.
class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(User,related_name='transfer_sent', on_delete=models.CASCADE, verbose_name='От пользователя')
    to_user = models.ForeignKey(User,related_name='transfer_received', on_delete=models.CASCADE, verbose_name='К пользователю')
    is_completed = models.BooleanField(default=False, verbose_name='Статус выпонения')
    amount = models.PositiveIntegerField(verbose_name='Сумма', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.from_user} отправлено {self.to_user}"

    User = get_user_model()

    def make_transfer(from_wallet, to_wallet, amount):
        try:
            from_user = User.objects.get(wallet_address=from_wallet)
            to_user = User.objects.get(wallet_address=to_wallet)
        except User.DoesNotExist:
            raise ValueError("Пользователь с указанным кошельком не найден")

        if from_user.balance >= amount:
            from_user.balance -= amount
            to_user.balance += amount
            from_user.save()
            to_user.save()

            HistoryTransfer.objects.create(from_user=from_user, to_user=to_user, amount=amount)
        else:
            raise ValueError("Недостаточно средств для выполнения перевода")

    
    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'
