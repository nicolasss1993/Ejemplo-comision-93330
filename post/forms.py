from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "autor", "contenido", "tags", "imagen", "publicado")
