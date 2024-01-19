import json
import pprint

import os
# 스크립트 파일의 디렉토리 경로 가져오기
script_directory = os.path.dirname(os.path.realpath(__file__))

# 현재 작업 디렉토리를 스크립트 파일의 디렉토리로 변경
os.chdir(script_directory)



def best_book(books_list):
    # 여기에 코드를 작성합니다.
    book_point = [] # book 의 sales point 를 모아둠
    for i in books_list:
        book_point.append(i['customerReviewRank'])

    for j in books_list:    
        if j['customerReviewRank'] == max(book_point):
            best_book_title = j['title']

    return best_book_title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    pprint.pprint(best_book(books_list))
