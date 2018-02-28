from django.shortcuts import render, get_object_or_404
from datetime import date

# Create your views here.
from .models import Events, Types


def events_list(request):
    context = {}
    context['past_events'] = Events.objects.all().filter(date__lt=date.today())
    context['upcoming_events'] = Events.objects.all().filter(date__gte=date.today()).order_by('date')
    return render(request, "all_events.html", context=context)


def event(request, event_id):
    context = {}
    context['event'] = get_object_or_404(Events, id=event_id)
    return render(request, "event.html", context=context)


def types (request, type_id):
    _type = get_object_or_404(Types, id=type_id)
    context ={}
    context['type'] = _type
    context['belongs_to'] = _type.belongsTo.all()
    return render(request, "types.html", context=context)
