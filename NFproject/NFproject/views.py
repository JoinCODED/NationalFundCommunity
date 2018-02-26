from django.shortcuts import render

from articles.models import Article, Category


def home(request):
    context = {}
    context['articles'] = Article.objects.all()
    context['featured_articles'] = Article.objects.filter(featured=True)
    context['categories'] = Category.objects.all()
    return render(request, "home.html", context=context)
