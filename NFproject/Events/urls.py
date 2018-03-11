from django.urls import path

from Events import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<event_slug>/update', views.update, name="update"),
    path('<int:event_id>/delete', views.delete, name="delete"),
    path('<event_slug>', views.event, name='event'),
    path('<event_slug>/register/',
         views.register, name='register'),
    path('<event_slug>/unregister',
         views.unregister, name='unregister'),
    path('types/<type_slug>', views.types, name='type')]
