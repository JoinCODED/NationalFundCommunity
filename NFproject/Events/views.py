from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone

from .models import Events, Types
from .forms import EventForm


def add(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                new_event = form.save()
                return redirect(new_event)
        else:

            form = EventForm()
            context = {"form": form}
            return render(request, "add_event.html", context)
    else:
        raise PermissionDenied


def update(request, event_slug):
    if request.user.is_superuser:
        event = Events.objects.get(slug=event_slug)

        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES, instance=event)
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
    else:
        raise PermissionDenied


def delete(request, event_id):
    Events.objects.get(id=event_id).delete()
    return redirect('events:index')


def index(request):
    context = {}
    query = request.GET.get('q')
    all_events = Events.objects.all()
    if query:
        all_events = all_events.filter(Q(title__icontains=query) |
                                       Q(organizer__icontains=query) |
                                       Q(content__icontains=query)).distinct()
    context['past_events'] = all_events.filter(date__lt=timezone.now())
    context['upcoming_events'] = all_events.filter(date__gte=timezone.now()) \
                                           .order_by('date')

    return render(request, "all_events.html", context=context)


def register(request, event_slug):
    if not request.user.is_authenticated:
        return redirect('signup')
    if request.user.is_organization:
        raise PermissionDenied
    event = get_object_or_404(Events, slug=event_slug)
    if request.user in event.attendees.all():
        event.attendees.remove(request.user)
        is_registerd = False
        
    else:
        if event.seats_remaining:
            event.attendees.add(request.user)
            is_registerd = True
        else:
            raise PermissionDenied
   

    data = {
        'is_registerd': is_registerd,
        'remaining_seats': event.seats_remaining
    }
    return JsonResponse(data)



def event(request, event_slug):
    context = {}
    context['registration_closed']= False
    event = get_object_or_404(Events, slug=event_slug)
    context['event'] = event
    isregistered = request.user in event.attendees.all()
    context['isregistered'] = isregistered
    registration_deadline = event.registration_deadline
    event_date = event.date
    if registration_deadline < timezone.now() or event_date < timezone.now():
        context['registration_closed'] = True  
    location = event.location_url.split('/')[6]
    lat = location.split(',')[0][1:]
    lng = location.split(',')[1]
    context['lat']= lat
    context['lng']= lng
    return render(request, "event.html", context=context)


def types(request, type_slug):
    _type = get_object_or_404(Types, slug=type_slug)
    context = {}
    context['type'] = _type
    context['belongs_to'] = _type.belongsTo.all()
    return render(request, "types.html", context=context)
