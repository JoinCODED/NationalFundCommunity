from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Profile

def profile(request, user_slug):
    context = {}
    context['profile'] = get_object_or_404(Profile, slug=user_slug)
    return render(request, "profile.html", context=context)

def profile_list(request):
    _profile_list = Profile.objects.all()
    type_filter= request.GET.get('type')
    if type_filter is not None:
        _profile_list=_profile_list.filter(type=type_filter)
    context = {}
    context['x'] = _profile_list
    return render(request, "all_profiles.html", context=context)
