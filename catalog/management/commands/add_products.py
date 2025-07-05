from django.core.management.base import BaseCommand

from catalog.models import Category, Product  # Импортируйте ваши модели здесь


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **options):
        self.stdout.write("Deleting existing data...")
        # Удаляем все объекты категорий и продуктов
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Добавляем тестовую категорию
        electronics_category = Category.objects.create(
            name="Electronics", description="Test electronic goods"
        )
        clothing_category = Category.objects.create(
            name="Clothing", description="Test clothes"
        )

        # Добавляем тестовые товары
        Product.objects.create(
            category=electronics_category,
            title="Samsung TV",
            price=599.99,
            stock_quantity=10,
        )
        Product.objects.create(
            category=clothing_category,
            title="Men's Jeans",
            price=39.99,
            stock_quantity=20,
        )
        Product.objects.create(
            category=electronics_category,
            title="Apple iPhone",
            price=999.99,
            stock_quantity=5,
        )

        self.stdout.write(self.style.SUCCESS("Successfully added test products!"))
