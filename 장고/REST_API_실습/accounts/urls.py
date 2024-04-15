from django.urls import path
from . import views

# 1. 회원가입 (POST) user 생성
# 2. 로그인 (POST) 세션 생성
# 3. 로그아웃 (POST) 세션 삭제
# 4. 유저가 작성한 articles (GET)

app_name = 'accounts'
urlpatterns = [
     path('signup/', views.signup, name = 'signup'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),

     # 계층 구조 표현 user 가 작성한 -> article
     path('<str:username>/articles/', views.article_list, name='article_list'),
]
