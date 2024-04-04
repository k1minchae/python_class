from django.contrib import admin
from django.urls import path
from . import views

app_name = 'stores'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:store_pk>/', views.detail, name = 'detail'),
    path('create/', views.create, name = 'create'),
    path('<int:store_pk>/add_product/', views.add_product, name = 'add_product'),
    path('<int:store_pk>/delete/<int:product_pk>/', views.delete_product, name = 'delete_product'),
]
