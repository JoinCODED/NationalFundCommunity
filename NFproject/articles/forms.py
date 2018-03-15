from django import forms

from .models import Article, Comments


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'picture', 'category']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
