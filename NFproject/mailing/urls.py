from django.urls import path

from mailing import views

app_name = 'mailing'
urlpatterns = [
    path('add/', views.add, name='add'),
]