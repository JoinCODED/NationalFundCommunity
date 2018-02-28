from django.shortcuts import render, get_object_or_404

from .models import Article, Category



def article_list(request):
    context = {}
    context['articles'] = Article.objects.all()
    return render(request, "index.html", context=context)


def article(request, article_slug):
    _article= get_object_or_404(Article, slug=article_slug)
    context = {}
    context['article'] = _article
    context ['article_categories']= _article.category.all()
    return render(request, "article.html", context=context)


def category(request, category_slug):
    _category=get_object_or_404(Category, slug=category_slug)
    context = {}
    context['category'] = _category
    context['categoriesOfArticles']=_category.categoriesOfArticles.all()
    return render(request, 'category.html', context=context)
