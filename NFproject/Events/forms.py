from django import forms
from django.forms.widgets import SelectDateWidget

from .models import Events


class EventForm(forms.ModelForm):    

    class Meta:
        model = Events
        fields = ['organizer', 'title', 'content', 'picture',
                  'date','registration_deadline', 'event_type', 'location_url', 'location_name','maximum_attendees']
        widgets={
            'registration_deadline': forms.DateInput(attrs={'type':'date'}),
            'date': forms.DateInput(attrs={'type':'date'})
        }