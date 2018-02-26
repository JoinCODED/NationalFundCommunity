from django.urls import path

from articles import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>', views.article, name='article'),
    path('categories/<int:category_id>', views.category, name='category')]
