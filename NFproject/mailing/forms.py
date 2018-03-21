from django import forms
from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = {'email'}
        labels = { 'email' :'SUBSCRIBE TO RECEIVE UPDATES',}
        