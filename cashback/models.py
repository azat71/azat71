from django.db import models
from sale.models import Sale
from client.models import Client


class CashBack(models.Model):
    sale = models.ForeignKey(Sale, verbose_name='Продажи', on_delete=models.CASCADE)
    cashback = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общий кэш', blank=True)


class CashAdd(models.Model):
    cash_add = models.ForeignKey(CashBack, verbose_name='кэш', on_delete=models.CASCADE, blank=True, null=True)
    total_cash = models.ForeignKey(Client, verbose_name='Общий Кэшбек', on_delete=models.CASCADE, blank=True, null=True)
