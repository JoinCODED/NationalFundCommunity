from django.shortcuts import render
from rest_framework import viewsets
from articles.models import Article
from .serializers import ArticleSerializer
# Create your views here.

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer