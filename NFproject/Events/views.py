from django.shortcuts import render,redirect,get_object_or_404
from datetime import date

# Create your views here.
from .models import Events, Types
from .forms import EventForm

def add_event(request):
    if request.method =='POST':
        form= EventForm(request.POST)
        if form.is_valid():
            new_event= form.save()
            return redirect(new_event)
    else:

        form = EventForm()
        context = {"form": form}
        return render (request,"add_event.html",context)

def events_list(request):
    context = {}
    context['past_events'] = Events.objects.all().filter(date__lt=date.today())
    context['upcoming_events'] = Events.objects.all().filter(date__gte=date.today()).order_by('date')
    return render(request, "all_events.html", context=context)


def event(request, event_slug):
    context = {}
    context['event'] = get_object_or_404(Events, slug=event_slug)
    return render(request, "event.html", context=context)


def types (request, type_slug):
    _type = get_object_or_404(Types, slug=type_slug)
    context ={}
    context['type'] = _type
    context['belongs_to'] = _type.belongsTo.all()
    return render(request, "types.html", context=context)
