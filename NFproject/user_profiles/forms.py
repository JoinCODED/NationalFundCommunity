from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Individual, Organization


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class IndividualSignupForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Individual
        fields = ['first_name', 'last_name', 'age', 'interest', 'bio', 'website']


class OrganizationSignupForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['company_name', 'location_URL', 'bio', 'website']
