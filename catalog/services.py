from django.core.cache import cache
from .models import Product


def get_products_by_category(category):
    key = f'products_category_{category.pk}'
    products = cache.get(key)
    if products is None:
        products = Product.objects.filter(category=category, is_published=True)
        cache.set(key, products, 60 * 15)
    return products

def get_all_products():
    key = 'all_products'
    products = cache.get(key)
    if products is None:
        products = Product.objects.filter(is_published=True)
        cache.set(key, products, 60 * 10)
    return products
