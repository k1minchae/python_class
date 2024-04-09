from django.contrib import admin
from django.urls import path
from . import views

app_name ='libraries'
urlpatterns = [
    path('books/', views.books, name='books'),
    path('create_author/', views.create_author, name='create_author'),
    
]
