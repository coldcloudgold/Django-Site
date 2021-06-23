from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Posts"
    verbose_name = "Пост"
    verbose_name_plural = "Посты"

    def ready(self):

        try:
            import os
            from django.contrib.auth import get_user_model

            User = get_user_model()

            if not User.objects.filter(username="admin").exists():
                user = User.objects.create_user(
                    username=os.environ.get("ADMIN_NAME", "admin"),
                    password=os.environ.get("ADMIN_PASSWORD", "admin"),
                )
                user.is_superuser = True
                user.is_staff = True
                user.save()
        except Exception as exc:
            pass
