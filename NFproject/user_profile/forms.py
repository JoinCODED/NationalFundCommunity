from django import forms
from .models import Individual_Profile,Orginization_Profile




class IndividualProfileForm (forms.ModelForm):

    class Meta:
        model =Individual_Profile
        fields =['bio','my_website','age','interest']

class OrginizationProfileForm (forms.ModelForm):

    class Meta:
        model =Orginization_Profile
        fields =['bio','my_website','location_name','location_URL']
