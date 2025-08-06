from django.db import models

from users.models import CustomUser


class BlogPost(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Содержимое")
    preview = models.ImageField("Превью", upload_to='blog_previews/', blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    views = models.PositiveIntegerField("Количество просмотров", default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        permissions = [
            ("can_manage_blog", "Может управлять содержимым блога"),
        ]

    def __str__(self):
        return self.title