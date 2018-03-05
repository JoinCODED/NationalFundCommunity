from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from .forms import ProfileForm
from django.urls import reverse

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

def signup (request):
    user_form=UserCreationForm(request.POST)
    profile_form=ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        user=user_form.save()
        profile=profile_form.save(commit=False) # create the profile but dont save in database yet
        profile.user= user # connect profile to user
        profile.save() # save the profile in database
        password = user_form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=password)
        login(request, user)
        return redirect(reverse('profile',args=[profile.slug]))
    else:
        return render (request,'signup.html',{"user_form":user_form,"profile_form":profile_form})
