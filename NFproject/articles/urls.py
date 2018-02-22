from articles import views
from django.urls import path


urlpatterns = [
    path('', views.all_articles, name='all_articles'),
    path('<int:article_id>', views.article, name='article'),
    path('category/<int:category_id>', views.category, name='category')]
