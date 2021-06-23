from django.urls import path
from .views import *

urlpatterns = [
    path("", LatestPostsFeed(), name="post_feed")
]
