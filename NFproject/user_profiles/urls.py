from django.urls import path

from user_profiles import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<username>', views.profile, name='profile'),
    # path('complete_profile/', views.complete_profile, name='complete_profile'),
]
