from django.shortcuts import render

from articles.models import Article, Category
from Events.models import Events
from datetime import date


def home(request):
    context = {}
    context['articles'] = Article.objects.all()
    context['featured_articles'] = Article.objects.filter(featured=True)
    context['categories'] = Category.objects.all()
    context['upcoming_events'] = Events.objects.all().filter(date__gte=date.today()).order_by('date')
    return render(request, "home.html", context=context)
