from django.urls import path

from user_profiles import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('edit_profile/<username>', views.update_profile, name='update_profile'),
    path('<username>', views.profile, name='profile'),
]
