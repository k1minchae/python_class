from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('<int:user_pk>/signout/', views.signout, name = 'signout'),
    path('<int:user_pk>/update/', views.update, name = 'update'),
    path('<int:user_pk>/password/', views.password_change, name = 'password_change'),
]