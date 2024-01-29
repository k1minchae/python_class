"""
문제 : 
예시화면과 동일한 결과가 될 수 있도록 형변환을 사용하여 코드를 수정하시오.

예시 화면 : 
현재 보유 중인 총 책의 수는 다음과 같습니다.
10
그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.
7

주어진 값 : 
book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
print(book * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(total - rental)
"""

# 풀이
book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
print(int(book) * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(total - int(rental))
