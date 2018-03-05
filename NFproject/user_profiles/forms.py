from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Individual, Organization


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class IndividualSignupForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['age', 'interest', 'bio', 'website']


class OrganizationSignupForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['company_name', 'location_URL', 'bio', 'website']
