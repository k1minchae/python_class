import json
import pprint

import os
# 스크립트 파일의 디렉토리 경로 가져오기
script_directory = os.path.dirname(os.path.realpath(__file__))

# 현재 작업 디렉토리를 스크립트 파일의 디렉토리로 변경
os.chdir(script_directory)


def books_info(books, categories):
    # 여기에 코드를 작성합니다.
    book_list = []
    for i in books:
        book_dict = {}
        book_dict["id"] = i["id"]
        book_dict["title"] = i["title"]
        book_dict['author'] = i['author']
        book_dict['priceSales'] = i['priceSales']
        book_dict['description'] = i['description']
        book_dict['cover'] = i['cover']

        category_name = []
        for categories in categories_list:
            if categories['id'] == i['categoryId'][0]:
                category_name.append(categories['name'])
            elif categories['id'] == i['categoryId'][1]:
                category_name.append(categories['name'])
        book_dict['categoryName'] = category_name
        book_list.append(book_dict)

    return book_list
   



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)
    pprint.pprint(books_info(books, categories_list))
    
