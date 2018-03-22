from django.shortcuts import render,redirect
from mailing.models import Subscriber
from mailing.forms import SubscribeForm
from articles.models import Article
from Events.models import Events
from datetime import date


def home(request):
    context = {}
    context['articles'] = Article.objects.all()
    context['featured_articles'] = Article.objects.filter(featured=True)
    context['upcoming_events'] = Events.objects.all() \
                                       .filter(date__gte=date.today()) \
                                       .order_by('date')
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            print("here")
            return redirect('home')
    else:
        form = SubscribeForm()
        context['form'] = form
        return render(request, "home.html", context=context)
