import logging

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView

from .models import Post, Comment, Follow, User
from .forms import PostForm, CommentForm

from .service.business_views import paginate

logger = logging.getLogger(__name__)


class IndexListView(ListView):
    queryset = Post.objects.filter(is_pub=True)
    paginate_by = 10
    template_name = "index_and_follow.html"
    extra_context = {
        "title": "Последние обновления на сайте",
        "header": "Последние обновления на сайте",
        "type_page": "index",
    }


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_or_update_post.html"
    extra_context = {
        "title": "Добавить запись",
        "header": "Создать новую запись",
        "button": "Добавить",
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"username": self.request.user.username})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_or_update_post.html"
    extra_context = {
        "title": "Редактировать запись",
        "header": "Обновить запись",
        "button": "Сохранить",
    }

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(author=user)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"username": self.request.user.username})


class PostDeleteView(DeleteView):
    model = Post

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(author=user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"username": self.request.user.username})


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "posts/create_comments.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs.get("pk")
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "post",
            kwargs={
                "username": self.request.user.username,
                "pk": self.kwargs.get("pk"),
            },
        )


class ProfileView(View):
    def get(self, request, username):
        author = get_object_or_404(User, username=username)
        posts = Post.objects.filter(author=author, is_pub=True)
        if request.user.is_authenticated:
            following = Follow.objects.filter(user=request.user, author=author)
        else:
            following = False
        data = paginate(posts, request, count=10)
        context = {
            "author": author,
            "following": following,
        }
        context.update(data)

        return render(request, "profile.html", context)


class CheckView(View):
    def get(self, request, username):
        posts = Post.objects.filter(author=request.user, is_pub=False)
        data = paginate(posts, request, count=10)
        context = {
            "author": request.user,
            "following": False,
            "check": True,
        }
        context.update(data)

        return render(request, "profile.html", context)


class FollowView(View):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        sub = user.follower.all().values_list("author")
        posts = Post.objects.filter(author__in=sub, is_pub=True)
        data = paginate(posts, request, count=10)

        return render(request, "index_and_follow.html", context=data)


def profile_follow(request, username):
    following_user = get_object_or_404(User, username=username)
    Follow.objects.get_or_create(user=request.user, author=following_user)

    return redirect("profile", following_user.username)


def profile_unfollow(request, username):
    unfollowing_user = get_object_or_404(User, username=username)
    unfollowing = get_object_or_404(Follow, user=request.user, author=unfollowing_user)
    unfollowing.delete()

    return redirect("profile", unfollowing_user.username)


def page_not_found(request, exception):
    logger.error(f"\n404\nПуть: {request.path}. Пользователь: {request.user.username}\n")
    return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)
