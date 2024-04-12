from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:movie_pk>/', views.detail, name = 'detail'),
    path('create/', views.create, name = 'create'),
    path('<int:movie_pk>/update/', views.update, name = 'update'),
    path('<int:movie_pk>/create_comment/', views.create_comment, name = 'create_comment'),
    path('<int:movie_pk>/delete/', views.delete, name = 'delete'),
    path('<int:movie_pk>/delete_comment/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
    
]