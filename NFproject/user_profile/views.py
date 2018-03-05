from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import IndividualProfileForm, OrginizationProfileForm
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.
from .models import Individual_Profile,Orginization_Profile

def profile(request, username):
    context = {}
    user = get_object_or_404(User, username=username)
    context['current_user'] = request.user.username == username
    if hasattr(user,'individual_profile'):
        context['profile'] = user.individual_profile
    else:
        context['profile'] = user.orginization_profile
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
