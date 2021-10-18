from django.urls import path
from api import views

urlpatterns = [
    path('get/', views.getArticles),
    path('create/', views.createArticle),
    path('articles/', views.ArticleListView.as_view()),
    path('articles/<int:pk>', views.ArticleDetailview.as_view()),

]