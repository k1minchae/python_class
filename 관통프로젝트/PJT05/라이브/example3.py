import requests
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
    for g in g_list:
        # 요소 안에서 해당 클래스를 (전부) 가진 특정 요소 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")

        # 요소가 존재한다면
        if title is not None:
            print('제목 = ', title.text)

key_word = '탕수육'
get_data(key_word)
