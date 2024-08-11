from django.db import models
from django.contrib.auth.models import User
from phone.models import Phone


class CartQueryset(models.QuerySet):

    def get_total_price(self):
        return sum(item.phone_price() for item in self)
    
    def get_total_quantity(self):
        if self:
            return sum(item.quantity for item in self)
        return

class Cart(models.Model):
    user = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.ForeignKey(to=Phone, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Телефон')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
        ordering = ("id",)

    objects = CartQueryset().as_manager()

    def phone_price(self):
        return round(self.phone.price * self.quantity, 2)


    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.phone.name} | Количество {self.quantity}'
            
        return f'Анонимная корзина | Товар {self.phone.name} | Количество {self.quantity}'
