from django.urls import path

from articles import views


app_name = 'articles'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='index'),
    path('add/', views.AddArticle.as_view(), name='add'),
    path('<slug>/update/',
         views.UpdateArticle.as_view(), name="update"),
    path('<int:pk>/delete/',
         views.DeleteArticle.as_view(), name="delete"),
    path('<article_slug>', views.article, name='article'),
    path('<article_slug>/comment/'),views.comment, name='comment'),
    path('<article_slug>/favorite/', views.favorite, name='favorite'),
    path('categories/<category_slug>', views.category, name='category')]
