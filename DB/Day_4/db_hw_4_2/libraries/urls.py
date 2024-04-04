from django.contrib import admin
from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:book_pk>/', views.detail, name = 'detail'),
    path('<int:book_pk>/create_comment', views.create_comment, name = 'create_comment'),
    path('<int:book_pk>/delete_comment/<int:comment_pk>/', views.delete_comment, name = 'delete_comment'),
]
