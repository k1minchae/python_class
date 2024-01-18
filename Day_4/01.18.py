''' 모듈 불러오기
import math     # import 를 통해 파일을 가져오는 것 필요

print(math.pi)  # 파이썬 어딘가에 math.py 가 저장되어있음
print(math.sqrt(4))    # 제곱근 구하는 함수

help(math)    # 내장 모듈 사용법 알려줌

from math import pi, sqrt   # 모듈 안에 있는 함수만 따로 불러오는 법
from my_math import sqrt
print(pi)
print(sqrt(4))
print(math.pi)
print(math.sqrt)

from math import *    # * 이 전체를 의미함 (전체다 import -> 비권장)
from math import pi, sqrt    
from my_math import sqrt    # 문제 발생
# -> math import 로 했으면 충돌X (math.sqrt // my_math.sqrt)
'''

# 모듈 불러오는 법 (내가 저장한 모듈)
# import my_math  # 동일한 경로에 있으면 바로 뜸
# print(my_math.add(1, 2))    # 3


''' if 문 형식
if 표현식:
    코드블록

elif 표현식:
    코드블록

else:
    코드블록
'''


# for 문의 형식
# for 변수 in 반복 가능한 객체:
#     코드블록


''' dict 반복문돌리면 ?
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key) # dict 는 반복돌리면 key만 나옴.
    print(my_dict[key]) # key도 출력하려면
'''

# 
# numbers = [4, 5, 10, -8, 5]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)  # [8, 10, 20, -16, 10]


'''중첩된 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:    # 안쪽 for 문 루프가 끝난 뒤 바깥쪽으로 넘어 감
        print(outer, inner)
# 출력 : A, c // A, d // B, c // B, d
'''

# 중첩 리스트 순회
# elements = [['A', 'B'], ['c', 'd']]

# for elem in elements:
#     for item in elem:  # print(elem) : ['A', 'B'] \n ['c', 'd']
#         print(item)    # print(item) : A \n B \n C \n D


'''while 문 예시
a = 0 

while < 3:      # 종료 조건에 다가가야해서 익숙치 않을 것
    print(a)
    a += 1      # a 가 3 이 되면 멈춤.

print('끝')     # while 문 밖에 있으므로 while 끝나면 실행 됨

# 출력 :
0
1
2
끝
'''

# 사용자 입력에 따른 반복
# number = int(input('양의 정수를 입력해주세요 : '))

# while number <= 0:
#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')
#     number = int(input('양의 정수를 입력해주세요. : ')) # 음수 넣을때마다 재입력 받음
# print('잘했습니다!')    # 양수 넣을경우 종료 및 프린트.

# '''
# 양의 정수를 입력해주세요 : -3
# 음수를 입력했습니다.
# 양의 정수를 입력해주세요. : 0
# 0은 양의 정수가 아닙니다.
# 양의 정수를 입력해주세요. : -2
# 음수를 입력했습니다.
# 양의 정수를 입력해주세요. : 3
# 잘했습니다!
# '''


'''while 에서Break 활용
number = int(input('양의 정수를 입력해주세요 : '))

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')     # 이스터에그 : 강제종료
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요. : ')) # 음수 넣을때마다 재입력 받음
print('잘했습니다!')    # 양수 넣을경우 종료 및 프린트.
'''

# for문에서의 break
# numbers = [1, 3, 5, 6, 7, 9, 19, 11]
# found_even = False  # 못찾을 때를 대비한

# for num in numbers:
#     if num % 2 == 0:
#         print('첫 번째 짝수를 찾았습니다:', num)
#         found_even = True
#         break   # 첫번째 짝수를 찾은 뒤 반복 종료하기.
# if not found_even:  
#     print('짝수를 찾지 못했습니다')

''' continue 활용
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue    # 짝수일 경우 print 로 넘어가지 않고 다음 반복으로 건너뜀
    print(num)

'''

# List Comprehension 활용
# 안 쓰고 하기
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []

# for num in numbers:
#     squared_numbers.append(num**2)

# print(squared_numbers)  # [1, 4, 9, 16, 25]


# # List comprehension 쓰기
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [num**2 for num in numbers]

# print(squared_numbers)  # [1, 4, 9, 16, 25]


'''if 의 사용
result = []
for i in range(10):
    if i % 2 == 1:
        result.append(i)

# List comprehension
result = [i for i in range(10) if i % 2 == 1]
'''

# 자주쓰는 모듈
# import random

# print(random.randint(1, 10)) # 1부터 10까지 랜덤 정수

# from random import *    # random.py 로부터 모든 method 를 가져온다. 
# print(randint(1, 10))   # ->random. 안써도됨

''' Jason Viewer
import requests
url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()
print(response)
'''

# 실습 : United States 를 출력해 보세요.
# import requests
# response = requests.get('https://random-data-api.com/api/v2/users').json()
# print(response['address']['country'])

''' IF 문 실습
dust = int(input())
    # if 조건식: 조건식이 True 일 경우 code실행
    # if 의 부정은 elif, elif 의 부정은 else
if dust > 150:  # if 150 >= dust dust > 80
    print('매우 나쁨')
elif dust > 80: 
    print('나쁨')
else:
    print('좋음')
'''

# 실습 문제 : 연도를 입력받아 윤년 판별하기. 윤년이면 'leap year' 출력
# 단, elif는 사용하지 마시오.
# 그렇지 않으면 'common year'출력.
# 1. 연도가 4로 나누어 떨어지지만 100으로는 나누어떨어지지 않는다.
# 2. 연도가 400으로 나누어 떨어진다.

# year = int(input())

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print('leap year')
# else:
#     print('common year')


''' for 문 실습 : 트리만들기
정수 n 을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램 작성

    # 내가 푼 것
n = int(input('n : '))

for i in range(1, 1 + n):
    print(i * '*')

    # 답
n = int(input('n : '))
for i in range(n):
    for j in range(i + 1):
        print('*', end= '')
    print()
'''

# 실습 1 : while 문 + continue를 사용하여 1~10 까지 정수중 홀수만 출력하기

# i = 0   # 초기식
# while i < 10: # 조건식 (i 가 10일 때 종료한다.)
#     i += 1  # 증감식
#     if i % 2 == 0:
#         continue
#     print(i, end = '')
#     print()

'''
break : 수행중인 반복문(for, while)을 강제로 종료하는 역할
실습 2 : 'shall we close? (y/n)' 문구에 y를 입력하면 반복문을 종료하고
'the end'를 출력하는 프로그램을 작성해보세요.


while True: # 무한 반복
    answer = input('shall we close? (y/n) ')
    if answer == 'y':
        print('the end')
        break
'''

# rows = int(input()) # 행
# cols = int(input()) # 열

# Comprehension 을 안 쓴 것.
# matrix = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(0)
#     matrix.append(row)

# Q) 2차원 리스트 컴프리헨션을 사용하여 0으로 초기화된 2차원 리스트 생성

# matrix = [[0 for _ in range(cols)] for _ in range(rows)]
# print(matrix)
# 열의 개수만큼 0 이 append 가 되고 행의 개수만큼 append됨
# comprehension을 쓰면 리스트를 초기화 할 필요가 없다.
# if 문 하고 같이 쓰는 것도 연습해보자.

''' Enumerate 예시
반복 되는 개체 각 요소에 대해 인덱스 값과 함께 반환하는 내장함수
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')

인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
'''
