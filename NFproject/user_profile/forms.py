from django import forms
from .models import Profile, IndividualProfile, OrginizationProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_type', 'website', 'bio']
        labels = {
            'profile_type': 'Account Type'
        }


class IndividualProfileForm (forms.ModelForm):
    class Meta:
        model = IndividualProfile
        fields = ['age', 'interest']


class OrginizationProfileForm (forms.ModelForm):
    class Meta:
        model = OrginizationProfile
        fields = ['company_name', 'location_URL']
