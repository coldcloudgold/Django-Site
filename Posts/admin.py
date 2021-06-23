from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("text", "pub_date", "author", "is_pub")
    search_fields = ("text",)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
