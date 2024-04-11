from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list),
    path('<int:book_pk>/', views.book_detail)
]
