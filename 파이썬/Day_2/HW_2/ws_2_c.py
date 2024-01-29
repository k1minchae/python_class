'''
문제 :
주어진 데이터 구조는 어떠한 API의 응답 결과이다. 
주어진 데이터 중 필요한 데이터만 출력할 수 있도록 코드 작성.

요구 사항 :
- 주어진 data 변수에 할당된 값에서 적절한 값을 찾아 새로운 데이터 생성
- first_data 변수에 비어있는 dict할당한다.
    a. '제목' key에 문제의 제목에 해당하는 값을 찾아 할당.
    b. '일자' key에는 일차에 해당하는 값을 '정수'로 할당
    c. '단계' key 에는 단계에 해당하는 값을 찾아 '{value}단계' 가 되도록 값 변경후 할당
    d. '과목' kye에는 과목에 해당하는 값을 찾아 할당.
-first_data 를 출력한다.
'''

# 주어진 코드
data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]

# 풀이 작성

first_data = {
    '제목': data[0]['results'][0]['properties']['제목']['title'][0]['plain_text'], 
    '일자': data[0]['results'][0]['properties']['일차']['number'], 
    '단계': str(data[0]['results'][0]['properties']['단계']['select']['name']) + '단계', 
    '과목': data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']
            }

print(first_data)