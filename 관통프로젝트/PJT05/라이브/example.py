import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/tag/love/"

# 1.다운로드 : url 을 이용해서 html 이 담긴 자료를 받아와야 함
response = requests.get(url)
# print(response) # <Response [200]> : 성공

html_txt = response.text # 페이지의 html 을 가져옴
# print(html_txt)
# print(type(html_txt)) # <class 'str'>

# 문자열 파싱은 코드로 짜기 복잡해서 라이브러리를 사용
soup = BeautifulSoup(html_txt, 'html.parser')
# print(type(soup)) # <class 'bs4.BeautifulSoup'> -> 사용할수있는 내장함수 포함

main = soup.find('a') # 첫번째 a태그 검색
# print(main.text) # Quotes to Scrape (text 안붙이면 요소전체가 나옴)

a_tags = soup.find_all('a') # 해당 태그를 가진 모든 요소 검색
# print(a_tags) # 리스트에 담겨져서 나옴

# find 보다 select 메서드가 좀더 범용적임 (웬만하면 class 나 id로 검색)
# CSS 선택자로 하나를 선택 -> 선택자가 일치하는 첫번째 글
word = soup.select_one('.text')
# print(f'첫 번째 글 : {word.text}')
# 첫 번째 글 : “It is better to be hated for what you are than to be loved for what you are not.”


# 모든 인용구 검색
words = soup.select('.text')
# for w in words:
    # print(f'글 : {w.text}')

