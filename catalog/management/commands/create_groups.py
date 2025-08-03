from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from blog.models import BlogPost
from catalog.models import Product
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Создает группы и назначает права'

    def handle(self, *args, **kwargs):
        # Модератор продуктов
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')
        content_type = ContentType.objects.get_for_model(Product)

        unpublish_perm = Permission.objects.get(codename='can_unpublish_product')
        delete_perm = Permission.objects.get(codename='delete_product')
        moderator_group.permissions.set([unpublish_perm, delete_perm])
        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" обновлена.'))

        # Контент-менеджер (для блога)
        content_group, created = Group.objects.get_or_create(name='Контент-менеджер')
        content_type = ContentType.objects.get_for_model(BlogPost)
        blog_perm = Permission.objects.filter(content_type__app_label='blog')
        content_group.permissions.set(blog_perm)
        self.stdout.write(self.style.SUCCESS('Группа "Контент-менеджер" обновлена.'))
