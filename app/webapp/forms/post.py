from django import forms

from ..models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'Tytuł artykułu',
            'content': 'Treść artykułu'
        }
