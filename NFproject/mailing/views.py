from django.shortcuts import render
from .models import Subscriber
from .forms import SubscribeForm
from django.views.generic import (CreateView)
# Create your views here.

class Subscribe(CreateView):
    model = Subscriber
    form_class = SubscribeForm
