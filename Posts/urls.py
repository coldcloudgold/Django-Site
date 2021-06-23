from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path("", cache_page(30)(IndexListView.as_view()), name="index"),
    path("follow/", login_required(FollowView.as_view()), name="follow_index"),
    path("new/", login_required(PostCreateView.as_view()), name="new_post"),
    path("<str:username>/", ProfileView.as_view(), name="profile"),
    path("<str:username>/check/", login_required(CheckView.as_view()), name="profile_check"),
    path("<str:username>/follow/", login_required(profile_follow), name="profile_follow"), 
    path("<str:username>/unfollow/", login_required(profile_unfollow), name="profile_unfollow"),
    path("<str:username>/<int:pk>/", PostDetailView.as_view(), name="post"),
    path("<str:username>/<int:pk>/edit/", login_required(PostUpdateView.as_view()), name="post_edit"),
    path("<str:username>/<int:pk>/delete/", login_required(PostDeleteView.as_view()), name="post_delete"),
    path("<str:username>/<int:pk>/comment", login_required(CommentCreateView.as_view()), name="add_comment"),
]
