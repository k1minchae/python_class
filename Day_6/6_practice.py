# my_set = {'a', 'b', 'c', 1, 2, 3}
# print(my_set)   # {1, 2, 3, 'a', 'b', 'c'} 순서가 없다.

# my_set.add(4)
# print(my_set)   # {'a', 1, 2, 3, 'c', 4, 'b'}

# my_set.add(4)
# print(my_set)   # {'a', 1, 2, 3, 'c', 4, 'b'}

# my_set.remove('a')
# print(my_set)   # {1, 2, 3, 4, 'b', 'c'}
# # my_set.remove('z')
# # print(my_set)   # KeyError: 'z'

# element = my_set.pop()  # my_set = {1, 2, 3, 4, 'c', 'b'}
# print(element)  # 1 이 가장 많이 나옴
# # 세트의 모습에 따라 어떤 값이 빠질 지 바뀜
# # 우리가 생각하는 랜덤의 확률과는 다르다.

# # my_set.clear()
# # print(my_set)   # set()

# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.update([1, 4, 5])
# print(my_set)   # {'c', 1, 2, 3, 'a', 4, 5, 'b'}
# # 1은 중복이라 들어가지 않음.

# my_set = {1, 2, 3}
# my_set.discard(1)
# print(my_set)    # {2, 3}

# my_set.discard('z') # 없는 값을 discard 하면 ?
# print(my_set)   # {2, 3} (오류 X)

'''
세트의 집합 메서드

set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}

print(set1.difference(set2))    # {0, 2, 4}
# set1 - set2 = (차집합) 반환

print(set1.intersection(set2))  # {1, 3}
# set1 & set2 (교집합) 반환

print(set1.issubset(set2))  # set1의 항목이 전부 set2에 종속되는지?
# set1 <= set2
# is로 시작하는 함수/메서드는 True/False값을 반환

print(set1.issuperset(set2)) # set1이 set2를 전부 포함하는지?
# set1 >= set2

print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
# set | set2 (합집합) 반환
'''

# 딕셔너리 메서드

# person = {
#         'name': 'Alice', 
#           'age': 25
# }

# # 1. D.get(x) : 키 값 반환
# print(person.get('name'))   # Alice
# print(person['name'])   # Alice


# print(person.get('country'))    # None
# # 키가 없을 경우 (Error X) None 반환
# # person['country'] 로 찾으면 에러가 난다.

# print(person.get('country', '기본값 : 키가 없습니다.')) # Unknown
# # 키가 없을 경우 키에 연결된 기본값 반환


# # 2. .keys() : 딕셔너리의 키를 모은 객체 반환
# print(person.keys())    # dict_keys(['name', 'age']) -> dict_keys type

# # 대괄호로 감싸져있음 (순서가 나열되어 있다. -> 반복 가능한 객체)
# for k in person.keys():
#     print(k)    
#     # name
#     # age

# print(person.values())
# # dict_values(['Alice', 25])

# for i in person.values():
#     print(i)    
#     # Alice
#     # 25

# print(person.items())
# # dict_items([('name', 'Alice'), ('age', 25)])

# for key, value in person.items():
#     print(key, value)
#     # name Alice
#     # age 25

# print(person.pop('name'))   # Alice -> 반환
# print(person)   # {'age': 25} -> 'name' 키/값 제거됨
# # print(person.pop('country'))    # KeyError
# print(person.pop('country', 'Default')) # Default


# person = {'name': 'Alice', 'age': 25}
# print(person.setdefault('country', 'Korea'))    # Korea
# print(person)   
# # {'name': 'Alice', 'age': 25, 'country': 'Korea'}



# person = {
#         'name': 'Alice', 
#           'age': 25
# }

# other_person = {
#     'name': 'Jane',
#     'gender': 'Female'
# }

# # other_person 에 있는 데이터를 person에 넣고싶다.
# person.update(other_person)
# print(person)   
# # 출력 : {'name': 'Jane', 'age': 25, 'gender': 'Female'}
# # 단, 중복된 key는 원본 값이 사라짐

# person.update(age= 50, country='korea')  # 키워드인자 사용 가능
# # 출력 : {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'korea'}
# print(person)

# person.clear()
# print(person)   # {}

'''
참고


list = [
    {'john': '521-1234'},
    {'Lisa': '521-8976'},
    {'Sandra': '521-9655'}
]
# 한번에 안 찾아짐 -> 검색 해야함 
# -> 길이가 길어질 수록 검색시간 길다.


dict = {
    'john': '521-1234',
    'Lisa': '521-8976',
    'Sandra': '521-9655'
}
print(dict.get('Lisa')) # key 가 많아도 한번에 찾아짐 


# 해시함수
print(hash(1))  # 1
print(hash(1))  # 1
print(hash('a'))    # 실행시마다 다름
print(hash('b'))    # 실행시마다 다름
      
'''

# 2 <- 테스트케이스
# 3 <- 3 x 3 행렬
# 1 2 3
# 4 5 6
# 7 8 9
# 2 <- 2 x 2 행렬
# 1 2 
# 3 4


# T = int(input())    
# for tc in range(1, T+1):
#     N = int(input())

#     arr = []    # 빈 리스트 사용
#     for _ in range(N):  # n x n 행렬 만들기 위해 순회
#         row = list(map(int, input().split()))
#         arr.append(row)

#     # arr = [list(map(int, input().split())) for _ in range(N)]
#     # 위의 for문으로 만든 것과 같다.

#     print(f'{tc} {result}')

'''
실습


my_dict = {
    'plus': ['더하기', '장점'],
    'minus': ['빼기', '적자'],
    'multiply': ['곱하기', '다양하게'],
    'division': ['나누기', '분열']
}

1. '빼기' 반환
print(my_dict.get('minus')[0])
print(my_dict['minus'][0])
print(my_dict.pop('minus')[0])
print(my_dict.setdefault('minus')[0]) 

2. key 값 순차적으로 출력
for i in my_dict.keys():
    print(i, end=' ')
print()

3. 'square' : ['제곱', '사각형'] 추가 (3가지 방법)
my_dict.setdefault('square', ['제곱', '사각형'])
my_dict.update(square = ['제곱', '사각형'])
my_dict['square'] = ['제곱', '사각형']

4. division 제거 (2가지 방법)
my_dict.pop('division')
del my_dict['division']
print(my_dict)
'''

#해시 테이블

# my_dict = {'a', 'b', 'c', 1, 2, 3}
# element = my_dict.pop()
# print(element)  # 정수는 1만 반환됨
# print(my_dict)  # 문자열의 경우 임의의 문자열 반환

# 정수는 고정된 해시코드를 가지고, 문자열의 해시코드는 일정하지 않다.
# hase() 함수 사용해보기

# print(hash(1))
# print(hash(2))
# print(hash('a'))
# print(hash('b'))

