from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Article, Category
from .forms import ArticleForm
from django.db.models import Q


def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                new_article = form.save()
                new_article.author = request.user
                new_article.save()
                return redirect(new_article)
        form = ArticleForm()
        context = {"form": form}
        return render(request, "add_article.html", context)
    else:
        raise PermissionDenied


def update(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    if article.author == request.user:

        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect(article)
        else:
            form = ArticleForm(instance=article)
            context = {
                "article": article,
                "form": form
            }
            return render(request, "update_article.html", context)
    else:
        raise PermissionDenied


def delete(request, article_id):
    Article.objects.get(id=article_id).delete()
    return redirect('articles:index')


def index(request):
    context = {}
    _articles = Article.objects.all()
    query = request.GET.get('q')
    if query:
        _articles = _articles.filter(Q(title__icontains=query) |
                                     Q(content__icontains=query) |
                                     Q(author_name__icontains=query)) \
                                     .distinct()
    context['articles'] = _articles
    return render(request, "index.html", context=context)


def article(request, article_slug):
    _article = get_object_or_404(Article, slug=article_slug)
    context = {}
    context['showUpdateBtn'] = _article.author == request.user
    context['article'] = _article
    context['article_categories'] = _article.category.all()
    return render(request, "article.html", context=context)


def category(request, category_slug):
    _category = get_object_or_404(Category, slug=category_slug)
    context = {}
    context['category'] = _category
    context['categoriesOfArticles'] = _category.categoriesOfArticles.all()
    return render(request, 'category.html', context=context)
