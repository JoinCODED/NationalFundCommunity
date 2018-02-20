from django.shortcuts import render, get_object_or_404
from .models import Article

def home (request):
    articleList = Article.objects.all()
    return render(request,"home.html",context={'articles':articleList})

def article (request,article_id):
    _article = get_object_or_404(Article, id = article_id)
    return render(request,"article.html",context={"article": _article})
