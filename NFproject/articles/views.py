from django.shortcuts import render, get_object_or_404

from .models import Article, Category


def get_categories():
    return Category.objects.all()


def article_list(request):
    context = {}
    context['articles'] = Article.objects.all()
    context['categories'] = get_categories()
    return render(request, "index.html", context=context)


def article(request, article_id):
    context = {}
    context['article'] = get_object_or_404(Article, id=article_id)
    context['categories'] = get_categories()
    return render(request, "article.html", context=context)


def category(request, category_id):
    context = {}
    context['category'] = get_object_or_404(Category, id=category_id)
    context['categories'] = get_categories()
    return render(request, 'category.html', context=context)
