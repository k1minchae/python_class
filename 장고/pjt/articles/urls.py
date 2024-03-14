from django.contrib import admin
from django.urls import path, include
from . import views
# 현재 디렉토리에 있는 views.py 를 불러온다는 뜻

app_name = 'articles'
urlpatterns = [
    path('', views.index),
    path('dinner/', views.dinner, name= 'dinner'),
    path('search/', views.search, name = 'search'),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name ="catch"),
    # variable routing
    path('articles/<int:num>/', views.detail, name = 'detail'),
]