from django.urls import path

from articles import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<article_slug>/update/',
         views.update, name="update"),
    path('<int:article_id>/delete/',
         views.delete, name="delete"),
    path('<article_slug>', views.article, name='article'),
    path('categories/<category_slug>', views.category, name='category')]
