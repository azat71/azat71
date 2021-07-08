from django.db import models
from branch.models import Branch
from user.models import User
from client.models import Client
from product.models import Product
from datetime import date


class Sale(models.Model):
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    branch = models.ForeignKey(Branch, verbose_name='Филиал', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE)


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, verbose_name='Продажи', on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    date = models.DateField(verbose_name='Дата', default=date.today)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена', blank=True)

    def __str__(self):
        return f"Продукт: {self.product.title} (для продаж)"

    def save(self, *args, **kwargs):
        self.final_price = self.amount * self.product.price
        super().save(*args, **kwargs)
