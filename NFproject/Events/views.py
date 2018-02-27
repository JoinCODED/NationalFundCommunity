from django.shortcuts import render, get_object_or_404
from datetime import date

# Create your views here.
from .models import Events

from articles.models import Category



def events_list(request):
    context = {}
    context['past_events'] = Events.objects.all().filter(date__lt=date.today()).order_by('-date')
    context['upcoming_events'] = Events.objects.all().filter(date__gte=date.today()).order_by('date')
    context['categories'] = Category.objects.all()
    return render(request, "all_events.html", context=context)


def event(request, event_id):
    context = {}
    context['event'] = get_object_or_404(Events, id=event_id)
    context['categories'] = Category.objects.all()
    return render(request, "event.html", context=context)
