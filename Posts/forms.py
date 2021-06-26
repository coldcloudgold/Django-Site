from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label="Содержание")

    class Meta:
        model = Post
        fields = ["title", "text", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text",]
