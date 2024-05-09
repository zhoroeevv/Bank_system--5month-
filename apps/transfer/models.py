from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
from apps.users.models import User

class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User, related_name='sent_user',
        on_delete= models.CASCADE,
        verbose_name="От пользователя",
        to_field='wallet_address'
    )
    to_user= models.ForeignKey(
        User, related_name='got_user',
        on_delete= models.CASCADE,
        verbose_name="От пользователя",
        to_field='wallet_address'
    )
    is_completed = models.BooleanField(
        default=False, 
        verbose_name="Перевод завершен"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания"
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Сумма перевода"
    )

    def __str__(self):
        return f"Перевод от {self.from_user.username} к {self.to_user.username}"
    def clean(self):
        super().clean()
        # Проверяем, достаточно ли у отправителя средств для выполнения перевода
        if self.from_user.balance < self.amount:
            # Если недостаточно средств, добавляем сообщение в non_field_errors
            self.add_error(None, "Недостаточно средств для перевода")
    
    
    def save(self, *args, **kwargs):
        # Проверяем, достаточно ли у отправителя средств для выполнения перевода
        if self.from_user.balance >= self.amount:
            # Вычитаем сумму перевода из баланса отправителя и добавляем ее получателю
            self.from_user.balance -= self.amount
            self.to_user.balance += self.amount
            # Сохраняем обновленные балансы пользователей
            self.from_user.save()
            self.to_user.save()
            super().save(*args, **kwargs)  # Сохраняем объект HistoryTransfer
        else:
            raise IntegrityError("Недостаточно средств для перевода")

    class Meta:
        verbose_name = "История перевода"
        verbose_name_plural = "История переводов"
