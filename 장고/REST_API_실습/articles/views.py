from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 데이터가 제대로 안되어있을 때 반환될 것 작성
        return Response(serializer.errors)
    elif request.method == 'GET':
        # DB에서 articles 전체 조회
        articles = Article.objects.all()
        # JSON 으로 포장 -> return
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
