from django.urls import path

from user_profiles import views

app_name ='profiles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<username>/update', views.update, name='update'),
    path('<username>', views.profile, name='profile'),
]
