from django.contrib import admin
from django.urls import path
from . import views

app_name ='libraries'
urlpatterns = [
    path('books/', views.books, name='books'),
    path('create_author/', views.create_author, name='create_author'),
    path('books/create/', views.create_book, name='create_book'),
    path('author_books/<int:author_pk>/', views.author_books, name='author_books'),
    path('author_books/subscribe/<int:author_pk>/', views.subscribe, name='subscribe'),
]
