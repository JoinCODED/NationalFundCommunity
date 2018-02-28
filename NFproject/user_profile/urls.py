from django.urls import path

from user_profile import views

urlpatterns = [
    path('<slug:user_slug>', views.profile, name='profile')]
