from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate

from .models import User, Individual, Organization
from .forms import CustomUserCreationForm, IndividualSignupForm, OrganizationSignupForm


def profile(request, username):
    context = {}
    user = get_object_or_404(User, username=username)
    context['current_user'] = request.user.id == user.id
    if user.is_individual:
        context['profile'] = user.individual
    elif user.is_organization:
        context['profile'] = user.organization
    return render(request, "profile.html", context)


def profile_list(request):
    pass
    # context = {}
    # indi_profile_list = Individual_Profile.objects.all()
    # orgi_profile_list= Organization_Profile.objects.all()
    # type_filter= request.GET.get('type')
    # if type_filter is not None and type_filter=='O':
    #     context['x']= orgi_profile_list
    #     context['y']= None
    # elif type_filter is not None and type_filter=='I':
    #     context['x']= indi_profile_list
    #     context['y']= None
    # else:
    #     context['x']= indi_profile_list
    #     context['y']= orgi_profile_list
    # return render(request, "all_profiles.html", context=context)


def create_profile(request, profile_form_class, type):
    user_form = CustomUserCreationForm(request.POST)
    profile_form = profile_form_class(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)
        setattr(user, f'is_{type}', True)
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


def signup(request):
    return render(request, 'signup.html')


def individual_signup(request):
    return create_profile(request, IndividualSignupForm, 'individual')


def organization_signup(request):
    return create_profile(request, OrganizationSignupForm, 'organization')
