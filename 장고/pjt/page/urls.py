from django.contrib import admin
from django.urls import path
from . import views
# 현재 디렉토리에 있는 views.py 를 불러온다는 뜻

app_name = 'page'
urlpatterns = [
    path('', views.index, name = "index"),
]