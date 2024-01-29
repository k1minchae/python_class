# """
# num1 = 5
# num2 = 3
# def get_sum(num1, num2):    # INPUT
#     '''이 함수는 두 수를 받아           # Docstring
#     두 수의 합을 반환하는 함수입니다.

#     >>>get_sum(1, 2)
#     3
#     '''
#     return num1 + num2  # OUTPUT
# sum_result = get_sum(num1, num2)    
# print(sum_result)

# # 함수 정의
# def greet(name):
#     '''입력된 이름 값에
#     인사를 하는 메세지를 만드는 함수
#     '''
#     message = 'hello' + name
#     return message

# # 함수 호출
# result = greet('Alice')
# print(result)

# # 함수 정의
# def add_numbers(x, y):   # x, y 는 매개변수
#     result = x + y
#     return result

# # 함수 호출
# a = 2
# b = 3
# sum_result = add_numbers(a,b)    # a, b는 인자
# print(sum_result)

# def greet(name, age):
#     print(f'안녕하세요, {name}님! {age}살 이시군요!')

# greet(age= 35, name = "Alice")    # 안녕하세요, Alice님! 35살 이시군요!
# greet(age = 35, 'Dave')    # 에러 발생
# # 위치인자 다음에 키워드인자를 써야함

# greet('Alice', 25)    # 안녕하세요, Alice님! 25살 이시군요!
# greet("Alice", 20, 30)
# # TypeError: greet() takes 2 positional arguments but 3 were given


# def calculate_sum(*args):    # 0개 이상 임의의 개수 처리한다는 뜻
#     print(args)
#     total = sum(args)
#     print(f'합계: {total}')s

# calculate_sum(1, 2, 3)

# (1, 2, 3)   # Tuple로 처리한다. (값 변경 불가)
# 합계: 6
# """
# '''
# def print_info(**kwargs):
#     print(kwargs)

# print_info(name='Eve', age = 30)
# # {'name': 'Eve', 'age': 30}
# '''

# '''
# def func(pos1, pos2, age=30, *args, **kwargs):
#     print(pos1, pos2, age, args, kwargs)

# func(1, 2, 3, 4, 5)    # 1 2 3 (4, 5) {}
# func(1, 2, 3, a=100, b=200) # 1 2 3 () {'a': 100, 'b': 200}


# def func():
#     num = 20
#     print('local', num) # local 20
# func()    # 여기서 num 변수가 죽음
# print('global', num)    # num이 정의되지 않았다고 뜸

# sum = 5    # 로컬에 sum 변수에 5 할당
# print(sum)    # 5
# print(sum(range(3)))    # 에러

# # 빌트인 순위가 마지막 순위이기 때문에 sum 함수를 못 쓰게 됨


# a = 1
# b = 2

# def enclosed():
#     a = 10
#     c = 3
    
#     def local(c):    # 정의
#         print(a, b, c)  # 10 2 500(호출될때 사용되므로)

#     local(500)  # 호출 -> 여기서 사용 (매개변수 500)
#     print(a, b, c)   # 10 2 3 -> enclosed함수

# enclosed()
# print(a, b) # 1 2 -> Global영역



# def factorial(n):
#     # 종료조건
#     if n == 0:
#         return 1
#     # 재귀호출
#     return n * factorial(n-1)   # 자기 자신 호출

# #계산 예시
# result = factorial(5)
# print(result)

# numbers = [1, 2, 3]
# result = map(str, numbers) # 함수의 이름만 쓴다.
# print(result)   # <map object at 0x0000021BEA5E4460>
# print(list(result))     # ['1', '2', '3']

# numbers = input().split()
# result = map(int, numbers) # map 객체로 생성
# list_result = list(result) # int를 가진 list로 생성
# print(list_result)


# girls = ['Jane', 'Ashely', 'Bella']
# boys = ['peter', 'jay']
# pair = zip(girls, boys)

# print(pair)
# print(list(pair))   # [('Jane', 'peter'), ('Ashely', 'jay')]



# numbers = [1, 2, 3, 4, 5]

# def func(x):
#     return x ** 2

# result = list(map(func, numbers))
# print(result)

# result2 = list(map(lambda x: x **2, numbers))
# print(result2)



# packed_values = 1, 2, 3, 4, 5
# print(packed_values)

# numbers = [1, 2, 3, 4, 5]
# a, *b, c = numbers

# print(a)    # 1
# print(b)    # [2, 3, 4] -> 남는 요소들을 리스트로 패킹
# print(c)    # 5


# print(packed_values)

# ---
# names = ['alice', 'jane', 'peter']
# print(names)    # ['alice', 'jane', 'peter']
# print(*names)   # alice jane peter



# def my_function(key1, key2, key3):
#     print(key1, key2, key3)

# my_dict = {'key1': 1, 'key2': 2, 'key3': 3}
# my_function(**my_dict)  # 1 2 3


# rows = int(input('행의 개수를 입력하세요'))
# matrix = []

# '''
# # 첫번째 방법
# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)  # 2차원 리스트의 형태로 matrix에 추가됨
# '''

# # 두번째 방법
# matrix = [list(map(int,input().split())) for _ in range(rows)]

# for row in matrix:
#     print(row)

# 방향 배열 
# def move_around(position):
#     x, y = position
#     direct = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상 하 좌 우


# 딕셔너리 실습

# my_dict = { # 중첩된 dict
#     'a1': {'b1': 1, 'b2': 2, 'b3': 3},
#     'a2': {'b1': 4, 'b2': 5, 'b3': 6},
#     'a3': {'b1': 7, 'b2': 8, 'b3': 9}
# }

# # value 5를 출력해보세요.
# print(my_dict['a2']['b2'])  # 5

# # method 사용하는 방법
# value = my_dict.get('a2').get('b2')
# print(value)

# 로또 6번호 추첨
# set(중복X), list(오름차순 정렬기능) 사용

# import random

# lottery = set()

# while len(lottery) <= 6:
#     number = random.randint(1, 45)
#     lottery.add(number)     # set 의 파이썬 내장함수

# lottery = list(lottery)
# lottery.sort()      # 오름차순 정렬
# print(*lottery)
'''
def get_sum(num1, num2):
    return num1 + num2

num1 = 5
num2 = 3
result = get_sum(num1, num2)
print(return)


# 실습 1. 매개변수가 없는 함수로 바꿔보세요.
def get_sum():
    num1 = 5
    num2 = 3
    return num1 + num2


result = get_sum()
print(result)


# 실습 2. 반환 값이 없는 함수로 바꿔보세요.
def get_sum(num1, num2):
    print(num1 + num2)

num1 = 5
num2 = 3
get_sum(num1, num2)
'''

# print((lambda x, y: x + y)(5,3))

# a, b, c = 1, 2, 3   # 글로벌
    
# def enclosed():
#     global a, b, c  # 서로 변수에 할당된 값을 공유 LEGB Rule에 의해 우선순위
#     a, b, c = 4, 5, 6

#     def local(c):
#         print(a, b, c)

#     local(500)  # 4 5 500
#     print(a, b, c)
# enclosed()   # 4 5 6
# print(a, b, c)  # 4 5 6 (로컬이 우선순위이기때문에)



''' zip함수
girls = ['Jane', 'Ashely']
boys = ['peter', 'jay']
pair = zip(girls, boys)

for i, j in pair:
    print(i, j)
'''




# packing / unpacking

# 1. 패킹 : 여러 값을 튜플로 묶는다.(X) - > 여러 값을 하나의 시퀀스(튜플) 로묶음

# 2. 언패킹
# 1번: * 를 언패킹 연산자로 활용 : 많이 씀
# names = ['kai', 'jane', 'bob']
# for name in names:
#     print(name, end = ' ')  # 출력: kai jane bob

# print(*names)   # *를 사용하여 unpacking

# 2번: dictionary unpacking : **사용

