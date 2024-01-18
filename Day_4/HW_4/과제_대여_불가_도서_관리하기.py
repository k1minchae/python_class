# 보유하지 않은 도서는 missing_book 리스트에 담는다.
# 리스트 컴프리헨션을 사용해라.

# 주어진 자료
list_of_book = [    # 보유중인 도서
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [ # 대여 예정 목록
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


missing_book = []

''' for 문을 사용한 방법
for i in rental_book:   # 보유하지 않은 도서 목록 만들기
    if i not in list_of_book:
        missing_book.append(i)
'''

# 리스트 컴프리헨션으로 바꾸기
missing_book = [i for i in rental_book if i not in list_of_book]


if missing_book == []:
    print('모든 도서가 대여 가능한 상태입니다.')
else:
    for j in missing_book:
        print(f'{j} 을/를 보충하여야 합니다.')