from django.urls import path

from articles import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('add_article/', views.add_article , name='add_article'),
    path('update_article/<slug:article_slug>', views.update_article, name="update_article"),
    path('<slug:article_slug>', views.article, name='article'),
    path('categories/<slug:category_slug>', views.category, name='category')]
