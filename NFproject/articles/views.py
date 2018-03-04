from django.shortcuts import render, redirect,get_object_or_404

from .models import Article, Category
from .forms import ArticleForm



def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save()
            return redirect(new_article)
    form = ArticleForm()
    context = {"form": form}
    return render(request,"add_article.html",context)

def update_article(request, article_slug):
    article = Article.objects.get(slug=article_slug)

    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES, instance=article)
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
