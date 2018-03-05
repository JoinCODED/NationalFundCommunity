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

# <li class="nav-item active">
# <a class="nav-link" href="{% url "profile_list" %}">Profiles<span class="sr-only"></span></a>
# </li>
# {%if profile_form.errors%}
# <div class="form-group has-error">
# <span class="help-block">{{profile_form.text.errors}}</span>
# </div>
# {% endif %}
#{{profile_form|crispy}}
