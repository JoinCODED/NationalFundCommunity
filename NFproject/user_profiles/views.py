from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate

from operator import attrgetter

from .models import User, Individual, Organization
from .forms import (CustomUserCreationForm, IndividualProfileForm,
                    OrganizationProfileForm)
# from articles.models import Article
# from Events.models import Events


def profile(request, username):
    context = {}
    user = get_object_or_404(User, username=username)
    # context['user_events']=Events.objects.all().filter(attendees=request.user)
    context['articles'] = user.articlesOfUser.all()
    if request.user.id == user.id:
        context['user_events'] = request.user.events.all()
    # context['articles']=Article.objects.all().filter(author__username=username)
    context['current_user'] = request.user.id == user.id
    if user.is_individual:
        context['profile'] = user.individual
        return render(request, "indi_profile.html", context)
    elif user.is_organization:
        context['profile'] = user.organization
        return render(request, "orgi_profile.html", context)


def profile_list(request):
    users = User.objects.all()

    type = request.GET.get('type')
    if type is not None:
        filter_dictionary = {f'is_{type}': True}
        users = users.filter(**filter_dictionary)

    profiles = []

    for user in users:
        if user.is_individual:
            profiles.append(user.individual)
        elif user.is_organization:
            profiles.append(user.organization)

    return render(request, 'all_profiles.html', {'profiles': profiles})


def create_profile(request, profile_form_class, type):
    user_form = CustomUserCreationForm(request.POST)
    profile_form = profile_form_class(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)

        if type == 'individual':
            user.is_individual = True
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
        elif type == 'organization':
            user.is_organization = True

        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        raw_password = user_form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(request, user)

        return redirect(profile)
    else:
        context = {"user_form": user_form, "profile_form": profile_form}
        return render(request, 'signup_profile.html', context)


def update_profile(request, username):
    user = User.objects.get(username=username)
    if user == request.user:
        if user.is_individual:
            form = IndividualProfileForm(request.POST or None,
                                         instance=user.individual)
        else:
            form = OrganizationProfileForm(request.POST or None,
                                           instance=user.organization)
        if form.is_valid():
            profile = form.save()
            return redirect(profile)
        else:
            context = {'form': form}
            return render(request, 'update_profile.html', context)
    else:
        raise PermissionDenied


def signup(request):
    return render(request, 'signup.html')


def individual_signup(request):
    return create_profile(request, IndividualProfileForm, 'individual')


def organization_signup(request):
    return create_profile(request, OrganizationProfileForm, 'organization')
