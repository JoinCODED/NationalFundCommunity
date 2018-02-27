from django.urls import path

from Events import views

urlpatterns = [
    path('', views.events_list, name='events_list'),
    path('<int:event_id>', views.event, name='event')]
