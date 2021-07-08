from django.db import models
from django.urls import reverse
from datetime import date
from django.core.validators import MinValueValidator


class TypeProduct(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип продукта')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('typeproduct_detail', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    type_product = models.ForeignKey(TypeProduct, verbose_name='Тип продукта', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение', null=True)
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', validators=[MinValueValidator(0)])
    date = models.DateField(verbose_name='Дата', default=date.today)
    percent_cashback = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
