from django.shortcuts import render
import requests
from .models import Article, Query
from bs4 import BeautifulSoup
from selenium import webdriver # 동적인 페이지 가져오기 + 자동화

def get_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"

    # response = requests.get(url)
    # print(response.text)

    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스들을 받아온다.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 각 게시물들을 가져오자!
    # 공통적으로 div 태그 + g클래스
    g_list = soup.select('div.g')
    result = []
    for g in g_list:
        # 요소 안에서 해당 클래스를 (전부) 가진 특정 요소 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")

        # 요소가 존재한다면
        if title is not None:
            result.append(title.text)
    return result

def crawling(request):
    keyword = '탕수육'
    titles = get_data(keyword)
    for title in titles:
        # 1. article, keyword저장
        # 2. 기존에 이미 저장된 거면 pass
        # get_or_create : 있다면 조회, 없다면 생성
        article, created_article = Article.objects.get_or_create(title=title)
        query_obj, created_query = Query.objects.get_or_create(article=article, keyword=keyword)

        