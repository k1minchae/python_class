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

    # 눈으로 보기좋게 출력
    # print(soup.prettify())

    # 파일로 저장하여 확인하는 법
    with open('soup.txt', 'w', encoding="utf-8") as file:
        file.write(soup.prettify())
key_word = '탕수육'
get_data(key_word)
