from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import IndividualProfileForm, OrginizationProfileForm
from django.urls import reverse

# Create your views here.
from .models import Individual_Profile,Orginization_Profile

# def profile(request, user_slug):
#     context = {}
#     context['profile'] = get_object_or_404(Profile, slug=user_slug)
#     return render(request, "profile.html", context=context)

# def profile_list(request):
#     _profile_list = Profile.objects.all()
#     type_filter= request.GET.get('type')
#     if type_filter is not None:
#         _profile_list=_profile_list.filter(type=type_filter)
#     context = {}
#     context['x'] = _profile_list
#     return render(request, "all_profiles.html", context=context)

def signup (request):
    user_form=UserCreationForm(request.POST)
    if user_form.is_valid():
        user=user_form.save()
        password = user_form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=password)
        login(request, user)
        type_choice=request.POST.get('type')
        if type_choice=="O":
            return redirect('orgin_form')
        else:
            return redirect('indi_form')
    else:
        return render (request,'signup.html',{"user_form":user_form})


def orgin_form (request):
    orginization_form= OrginizationProfileForm(request.POST)

    if orginization_form.is_valid():
        profile=orginization_form.save(commit=False)
        profile.user=request.user
        profile.save()
        return redirect('home')
        #return redirect(reverse('profile',orginization_form.slug))
    else:
        return render (request,'orgin_form.html',{"orginization_form":orginization_form})

def indi_form (request):
    individual_form= IndividualProfileForm(request.POST)
    if individual_form.is_valid():
        profile=individual_form.save(commit=False)
        profile.user=request.user
        profile.save()
        return redirect ('home')
        #return redirect(reverse('profile',individual_form.slug))
    else:
        return render (request,'indi_form.html',{"individual_form":individual_form})
