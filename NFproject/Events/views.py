from django.shortcuts import render,redirect,get_object_or_404
from datetime import date

# Create your views here.
from .models import Events, Types
from .forms import EventForm

def add_event(request):
    if request.method =='POST':
        form= EventForm(request.POST,request.FILES)
        if form.is_valid():
            new_event= form.save()
            return redirect(new_event)
    else:

        form = EventForm()
        context = {"form": form}
        return render (request,"add_event.html",context)

def update_event(request, event_slug):
    event = Events.objects.get(slug=event_slug)

    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES , instance=event)
        if form.is_valid():
            form.save()
            return redirect(event)
    else:
        form = EventForm(instance=event)
        context = {
            "event": event,
            "form": form
        }
        return render(request, "update_event.html", context)

def delete_event(request, event_id):
    Events.objects.get(id = event_id).delete()
    return redirect('events_list')

def events_list(request):
    context = {}
    context['past_events'] = Events.objects.all().filter(date__lt=date.today())
    context['upcoming_events'] = Events.objects.all().filter(date__gte=date.today()).order_by('date')
    return render(request, "all_events.html", context=context)

def register_to_event(request,event_slug):
    event = Events.objects.get(slug=event_slug)
    event.attendees.add(request.user)
    return redirect('events_list')

def unregister_to_event(request,event_slug):
    event = Events.objects.get(slug=event_slug)
    event.attendees.remove(request.user)
    return redirect('events_list')

def event(request, event_slug):
    context = {}
    event= get_object_or_404(Events, slug=event_slug)
    context['event'] = event
    isregistered= request.user in event.attendees.all()
    context['isregistered']=isregistered
    return render(request, "event.html", context=context)


def types (request, type_slug):
    _type = get_object_or_404(Types, slug=type_slug)
    context ={}
    context['type'] = _type
    context['belongs_to'] = _type.belongsTo.all()
    return render(request, "types.html", context=context)
