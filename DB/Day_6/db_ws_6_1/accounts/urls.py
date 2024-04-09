from django.contrib import admin
from django.urls import path
from . import views

app_name= 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('signout/', views.signout, name='signout'),
    path('profile/<str:username>/', views.profile, name='profile'),

]
