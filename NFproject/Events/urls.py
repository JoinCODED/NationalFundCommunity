from django.urls import path

from Events import views

urlpatterns = [
    path('', views.events_list, name='events_list'),
    path('add_event/', views.add_event , name='add_event'),
    path('update_event/<event_slug>', views.update_event, name="update_event"),
    path('delete_event/<int:event_id>', views.delete_event, name= "delete_event"),
    path('<event_slug>', views.event, name='event'),
    path('types/<type_slug>', views.types, name='type')]
