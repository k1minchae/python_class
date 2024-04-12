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

    # 검색 결과 개수는 result-status id를 사용
    result_stats = soup.select_one('#result-stats')
    print(result_stats.text) # 검색결과 약 6,740,000개 (0.26초) 


key_word = '탕수육'
get_data(key_word)
