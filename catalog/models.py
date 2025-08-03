from django.conf import settings
from unicodedata import category

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    ]
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="products/", verbose_name="Изображение")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
        ]

    def __str__(self):
        return self.name
