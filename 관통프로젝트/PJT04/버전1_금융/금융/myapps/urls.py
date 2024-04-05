from django.contrib import admin
from django.urls import path
from . import views

app_name = 'my_apps'
urlpatterns = [
    path('', views.index, name = 'index')
]
