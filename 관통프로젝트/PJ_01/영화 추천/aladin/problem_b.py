import json
from pprint import pprint


def book_info(book, categories):
    # 여기에 코드를 작성합니다.
    book_dict = {}
    book_dict["id"] = book["id"]
    book_dict["title"] = book["title"]
    book_dict['author'] = book['author']
    book_dict['priceSales'] = book['priceSales']
    book_dict['description'] = book['description']
    book_dict['cover'] = book['cover']

    category_name = []
    for categories in categories_list:
        if categories['id'] == book['categoryId'][0]:
            category_name.append(categories['name'])
        elif categories['id'] == book['categoryId'][1]:
            category_name.append(categories['name'])
    book_dict['categoryName'] = category_name


    return book_dict
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))

# 카테고리 목록
# [{'id': 31916, 'name': '과학'},
#  {'id': 31908, 'name': '에세이 / 수필'},
#  {'id': 151138, 'name': '자기계발'},
#  {'id': 153690, 'name': '서양철학'},
#  {'id': 151128, 'name': '문학'},
#  {'id': 50919, 'name': '영미소설'},
#  {'id': 89481, 'name': '외국 과학소설'},
#  {'id': 50922, 'name': '독일소설'},
#  {'id': 70216, 'name': '성공학'},
#  {'id': 51786, 'name': '육아 일반'},
#  {'id': 51082, 'name': '건축'},
#  {'id': 51381, 'name': '인문'},
#  {'id': 51260, 'name': '프랑스 문학'},
#  {'id': 50982, 'name': '미술사'},
#  {'id': 51545, 'name': '인류학'},
#  {'id': 51205, 'name': '생명과학'},
#  {'id': 51310, 'name': '우주과학'},
#  {'id': 50921, 'name': '철학'},
#  {'id': 51449, 'name': '윤리학'},
#  {'id': 2721, 'name': '컴퓨터 공학'}]