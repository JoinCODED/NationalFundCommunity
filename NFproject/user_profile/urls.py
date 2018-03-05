from django.urls import path

from user_profile import views

urlpatterns = [
    #path('', views.profile_list, name='profile_list'),
    #path('<slug:user_slug>', views.profile, name='profile')
    path('originization_info/', views.orgin_form, name='orgin_form'),
    path('individual_info/', views.indi_form, name='indi_form')

    ]
