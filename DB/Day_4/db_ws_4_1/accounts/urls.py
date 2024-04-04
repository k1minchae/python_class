from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('update/<int:user_pk>/', views.update, name = 'update'),
    path('update_staff/<int:user_pk>/', views.update_staff, name = 'update_staff'),
    path('delete/<int:user_pk>/', views.delete, name = 'delete'),
]
