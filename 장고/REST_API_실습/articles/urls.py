from django.urls import path
from . import views

# 1. 게시글 생성 (POST)
# 2. 게시글 전체 조회 (GET)
# => 대상이 하나이므로 url 하나만 만들기
app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='article_list'),
]
