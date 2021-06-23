from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Follow(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="follower")
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="following"
    )


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(max_length=140, verbose_name="Содержание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="post", verbose_name="Автор")
    image = models.ImageField(
        upload_to="posts_image/",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    is_pub = models.BooleanField(default=False, verbose_name="Опубликованно")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-created"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
