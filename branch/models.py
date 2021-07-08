from django.db import models
from django.urls import reverse
from user.models import User


class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название филиал')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, verbose_name='Продавец', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type_product_detail', kwargs={'slug': self.slug})