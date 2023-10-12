from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<slug:slug>/', views.edit_article, name='edit_article'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('article/delete/<slug:slug>/',
         views.delete_article, name='delete_article'),
    path('like/<slug:slug>/', views.like_article, name='like_article'),
]
