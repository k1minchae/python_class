from django.contrib import admin
from django.urls import path
from . import views

app_name = 'datas'
urlpatterns = [
    # path('dataframe/', views.dataframe, name='dataframe'),
    # path('missing-data/', views.missing_data, name='missing_data'),
    path('average-age/', views.average_age, name='average_age'),
]
