from django.urls import path

from Events import views

urlpatterns = [
    path('', views.events_list, name='events_list'),
    path('<slug:event_slug>', views.event, name='event'),
    path('types/<slug:type_slug>', views.types, name='type')]
