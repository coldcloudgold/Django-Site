from django.conf import settings
from Site.settings import STATIC_ROOT, STATIC_URL
from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("feed/", include("Feed_RSS.urls")),
    path("", include("Posts.urls")),
    path("about/", include("django.contrib.flatpages.urls")),
    path("author/", views.flatpage, {"url": "/author/"}, name="author"),
    path("spec/", views.flatpage, {"url": "/spec/"}, name="spec"),
    path("accounts/", include("Users.urls")),
    path("accounts/", include("allauth.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    from django.conf.urls import handler404, handler500

    handler404 = "Posts.views.page_not_found"
    handler500 = "Posts.views.server_error"
