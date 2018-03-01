from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Profile

def profile(request, user_slug):
    context = {}
    context['profile'] = get_object_or_404(Profile, slug=user_slug)
    return render(request, "profile.html", context=context)

def profile_list(request):
    context = {}
    context['x'] = Profile.objects.all()
    return render(request, "all_profiles.html", context=context)
