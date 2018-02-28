from django.urls import path

from articles import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:article_slug>', views.article, name='article'),
    path('categories/<slug:category_slug>', views.category, name='category')]
