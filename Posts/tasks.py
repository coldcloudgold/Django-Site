import os
from django.core.mail import send_mail
from celery import shared_task
from Posts.models import Post
from django.contrib.sites.models import Site


@shared_task
def send_check_post(subject="Уведомление", message="Проверка новых постов.", from_email=os.environ.get("DJANGO_EMAIL_HOST_USER"), to_email=os.environ.get("DJANGO_EMAIL_HOST_USER"), fail_silently=True):
    posts = Post.objects.filter(is_pub=False)
    site = Site.objects.get(pk=1).name
    if posts:
        counter = 1
        for post in posts:
            message += f"\n{counter}. Автор: http://{site}/{post.author.username}. Ссылка: http://{site}/{post.author.username}/{post.pk}/ Ссылка (админка): http://{site}/admin/Posts/post/{post.pk}/change/ "
            counter += 1
            
        return send_mail(subject, message, from_email, [to_email], fail_silently)
    return "Все посты проверены, сообщений не требуется."
