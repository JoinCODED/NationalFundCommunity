from django import forms
from django.forms.widgets import SelectDateWidget

from .models import Events


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Events
        fields = ['organizer', 'title', 'content', 'picture',
                  'date', 'event_type', 'location_url', 'location_name']
