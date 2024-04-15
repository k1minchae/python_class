from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer, UserArticleListSerializer
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# API 서버이기 때문에 이제는 render처럼 화면을 return 하지 않음
# 이제는 데이터를 json 타입으로 return 할 것
# Django -> Json -> Client : serializer사용
# 실제 데이터를 변환하는 것이 아니라 데이터를 json 으로 포장

@api_view(['POST'])
def signup(request):
    # request.data : 사용자가 전송한 데이터가 담겨있다.
    # serializer 를 통해 저장한다.
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    # 로그인 로직
    # django 내부적으로는 무슨일이 일어날까? -> session 생성 -> session_id 를 client 에게 전달
    username = request.data.get('username')
    password = request.data.get('password')
    # authenticate : 복호화, 암호화 기능 (password 가 암호화되어있음)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return Response({'message' :f'{username} 로그인 성공!'})
    else:
        return Response({'error': 'username 이나 password가 잘못되었습니다.'})
    

# django 내부 logout로직
# 쿠키에서 sessionID 삭제
# django-session 테이블에서 해당 유저의 세션 정보 삭제
@login_required
@api_view(['POST'])
def logout(request):
    message = {
        'message': f'{request.user} 가 로그아웃함'
    }
    auth_logout(request)
    return Response(message)

@api_view(['GET'])
def article_list(request, username):
    # username 을 이용해서 해당user 검색
    # 없는 데이터라면 '의도적으로' 404에러를 출력
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserArticleListSerializer(user)
    return Response(serializer.data)
    