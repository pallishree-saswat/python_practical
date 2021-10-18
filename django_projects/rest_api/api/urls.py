from django.urls import path
from django.urls.resolvers import URLPattern
from api import views

urlpatterns = [
    path('', views.ArticlesListView.as_view()),
    path('/<int:pk>', views.ArticleDetailView.as_view())
]