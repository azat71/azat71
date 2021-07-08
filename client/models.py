from django.db import models
from user.models import User
from django.core.validators import MinValueValidator


class Client(models.Model):
    user = models.OneToOneField(User, verbose_name='Клиент', on_delete=models.CASCADE)
    cashback_all = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])