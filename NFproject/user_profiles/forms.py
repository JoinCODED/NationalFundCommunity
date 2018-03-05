from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Individual, Orginization


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class IndividualSignupForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['age', 'interest']


class OrganizationSignupForm(forms.ModelForm):
    class Meta:
        model = Orginization
        fields = ['company_name', 'location_URL']
