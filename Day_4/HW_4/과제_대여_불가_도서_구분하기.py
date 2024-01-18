# 반복문 사용하기
# 주어진 리스트
list_of_book = [
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

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


if rental_list == list_of_book: # 만약 두 리스트가 동일하다면
        print('모든 도서가 대여 가능한 상태입니다.')
else:   # 그렇지 않으면 반복문으로 들어감.
    for i in rental_list:
        if i in list_of_book:   
            # rental_list의 요소가 list_of_book 에 있으면 다시 위로 올라감.
            continue
        else:   # list_of_book에 없다면, 보유하고 있지 않다고 출력후 break.
            print(f'{i} 은/는 보유하고 있지 않습니다.')
            break
        