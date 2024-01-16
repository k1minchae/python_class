'''
문제 : 
도서 목록을 다시 정리하던 중 이번엔 작가와 책을 연결시켜둔 자료가 뒤죽박죽이 됨.
파이썬의 딕셔너리를 활용하여 올바른 작가의 key값에 올바른 도서목록 리스트가
value로 할당될 수 있도록 코드를 작성하시오.
단, 작가 이름과 책 이름은 모두 authors, books 리스트에서 인덱스로 접근하여 
information dict 에 할당한다.

실행 결과 :
김시습 : ['금오신화', '이생규장전', '만복자서포기']
허균 : ['홍길동전', '장생전', '도문대작']
남영로 : ['옥루몽', '옥련몽']
작자 미상 : ['장화홍련전', '가락국 신화', '온달 설화']
임제 : ['수성지', '백호집', '원생몽유록']
'''
# 주어진 코드
information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

information[authors[1]] = books[3]

# 여기부터 입력

information[authors[0]] = books[1]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

print(f"김시습 : {information['김시습']}\n허균 : {information['허균']}\n남영로 : {information['남영로']}\n작자 미상 : {information['작자 미상']}\n임제 : {information['임제']}")