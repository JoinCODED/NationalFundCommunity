from django.shortcuts import render,redirect
from .models import Subscriber
from .forms import SubscribeForm
# Create your views here.

def add(request):
    if request.method == 'POST':
                form = SubscribeForm(request.POST)
                if form.is_valid():
                    form.save()
                    print("here")
                    return redirect('home')
    else:
        form = SubscribeForm()
        context = {"form": form}
        return render(request, "mailing/subscriber_form.html", context)

