from django.urls import path

from user_profile import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<slug:user_slug>', views.profile, name='profile')]
