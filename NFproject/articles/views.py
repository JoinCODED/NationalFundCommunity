from django.shortcuts import render, get_object_or_404
from .models import Article, Category
def get_categories ():
    return Category.objects.all()
def home (request):
    articleList = Article.objects.all().filter(featured=True)
    return render(request,"home.html",context={'articles':articleList,'categories':get_categories()})

def article (request,article_id):
    _article = get_object_or_404(Article, id = article_id)
    return render(request,"article.html",context={"article": _article,'categories':get_categories()})

def all_articles (request):
    articleList = Article.objects.all()
    return render(request,"all_Articles.html",context={'articles':articleList,'categories':get_categories()})
def category (request,category_id):
    _category = get_object_or_404(Category,id=category_id)
    return render (request,'category.html',context={'category':_category,'categories':get_categories()})
