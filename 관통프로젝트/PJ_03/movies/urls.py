from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name="index"),
    path('community/', views.community, name="community"),
]
