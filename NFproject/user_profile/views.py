from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.models import User

from .models import IndividualProfile, OrginizationProfile, Profile
from .forms import ProfileForm, IndividualProfileForm, OrginizationProfileForm


def profile(request, username):
    context = {}
    user = get_object_or_404(User, username=username)
    context['current_user'] = request.user.id == user.id
    # if hasattr(user, 'individual_profile'):
    #     context['profile'] = user.individual_profile
    # else:
    #     context['profile'] = user.orginization_profile
    return render(request, "profile.html", context=context)


def profile_list(request):
    context = {}
    indi_profile_list = Individual_Profile.objects.all()
    orgi_profile_list= Orginization_Profile.objects.all()
    type_filter= request.GET.get('type')
    if type_filter is not None and type_filter=='O':
        context['x']= orgi_profile_list
        context['y']= None
    elif type_filter is not None and type_filter=='I':
        context['x']= indi_profile_list
        context['y']= None
    else:
        context['x']= indi_profile_list
        context['y']= orgi_profile_list
    return render(request, "all_profiles.html", context=context)


def signup(request):
    user_form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        password = user_form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=password)
        login(request, user)

        return redirect('complete_profile')
    else:
        return render(request,
                      'signup.html',
                      {
                          "user_form": user_form,
                          "profile_form": profile_form
                      })


def complete_profile(request):
    profile = request.user.profile

    if profile.profile_type == "I":
        instance = IndividualProfile()
        instance.profile_ptr = profile
        form = IndividualProfileForm(request.POST, instance=instance)
    elif profile.profile_type == "O":
        instance = OrginizationProfile()
        instance.profile_ptr = profile
        form = OrginizationProfileForm(request.POST, instance=instance)

    if form.is_valid():
        instance.user = request.user
        sub_profile = form.save()
        return redirect(sub_profile)

    return render(request, 'complete_profile.html', {"form": form})
