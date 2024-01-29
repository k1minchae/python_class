'''메서드와 일반적인 함수의 차이
def append():
    pass

append()    # 함수 호출

my_list = []
my_list.append()    # 메서드 호출 -> 데이터 타입의 객체가 호출함.
# 객체.메서드()
'''

# my_str = 'banana'

# # find
# print(my_str.find('a')) # a의 첫번째 위치(인덱스)를 반환
# print(my_str.find('z')) # 없으면 -1을 반환

# # index
# print(my_str.index('a')) # a의 첫번째 인덱스 반환
# print(my_str.index('z')) # ValueError: substring not found


'''
# isalpha : 알파벳 문자로 구성되어 있는지 ?
string1 = 'Hello'
string2 = '123a'
print(string1.isalpha())
print(string2.isalpha())
'''

# split(분리) // join(결합)
# text = 'Hello, world!'
# new_text = text.split(',')
# print(new_text) # ['Hello', ' world!']

# words = ['Hello', 'world!']
# text= '-'.join(words)   # -를 기준으로 두 문자를 합침
# print(text) # 'Hello-world!


'''리스트 메서드 : 값 추가 / 삭제
my_list = [1, 2, 3]

# append
my_list.append(4)
my_list.append([5, 6, 7])   # 이건 풀려서 안들어감
print(my_list)

# .extend
my_list.extend([5, 6, 7])   # iterable 한 요소가 풀려서 들어감
print(my_list)


my_list = [1, 2, 3, 4, 5]
# insert
my_list.insert(3, 'ssafy')  # 인덱스 3에 'ssafy' 추가
print(my_list)

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
print(item1)    # 마지막 값 제거(5) + 반환

item2 = my_list.pop(0)
print(item2)    # 0번 인덱스 값(1) 제거

print(my_list)  # 마지막 값과 0번째 값이 제거된 상태로 출력
'''

# list 탐색 및 정렬 메서드
# index
# my_list = [1, 2, 3, 3, 3]
# index = my_list.index(3) # return 값이 있어서 변수에 할당 가능
# print(index) # 2

# # count
# my_list = [1, 2, 3, 3, 3]
# count = my_list.count(3)
# print(count)    # 3

# # sort
# my_list = [3, 2, 1]
# # 기본값: 오름차순
# sorted_list = my_list.sort()    
# print(sorted_list)  # None (반환값 X)
# print(my_list) # [1, 2, 3] 원본 값을 바꿔주기 때문.

# my_list.sort(reverse=True) # 내림차순
# # .sort() 는 sort(reverse=False) 상태임.
# print(my_list)  # [3, 2, 1]

# # reverse
# my_list = [1, 3, 2, 8, 1, 9]
# my_list.reverse()
# print(my_list)  # [9, 1, 8, 2, 3, 1]
# # 이것도 역시 반환값 X 

'''복사
변경가능한 데이터 타입의 복사

a = [1, 2, 3, 4]
b = a   # a, b 의 주소값이 같다. -> 할당
b[0] = 100 

print(a) # a도 바꼈을까? -> 같이 바뀜. [100, 2, 3, 4]
print(b) # b의 값은 당연히 바뀜 [100, 2, 3, 4]

a = 100
b = a

b = 9
print(a)    # 100 (안바뀜!★)
print(b)    # 9
'''

# 할당
# original_list = [1, 2, 3]
# copy_list = original_list # 할당

# copy_list[0] = 'hello'
# print(original_list)    # ['hello', 2, 3] (원본도 바뀜)


# 얕은 복사
# slicing : 자른 뒤 '새로운'리스트를 만듦 (주소값 달라짐)
# a = [1, 2, 3]   
# b = a[:]
# b[0] = 100

# print(a)    # 원본값이 바뀌지 않음

# 얕은 복사의 한계
# a = [1, 2, [1, 2]]
# b = a[:]

# b[2][0] = 100
# print(a) # [1, 2, [100, 2]] -> 2차원 리스트는 안 됨

# 깊은 복사
# import copy

# original_list = [1, 2, [3, 4]]
# deep_copied_list = copy.deepcopy(original_list) # deepcopy 함수 활용

# deep_copied_list[2][0] = 100

# print(original_list) # [1, 2, [3, 4]] 
# 2차원 리스트임에도 원본은 바뀌지 않음

'''
여기서부터 실습

오늘 배운 거 다 암기하기
문자열 메서드 -> IM형 : 문자열 파싱(parsing)
리스트 메서드 -> IM형 : 방향 배열


# 문자열 메서드 실습
# 문자열은 불변시퀀스라서 원본 안 바뀜.
# 구조 : 객체.method

a = ' Practice makes perfect '
# 1. 문자열 a 에서 e의 개수 세기 ★★★
count_e = a.count('e')
print(count_e)

# 2. 문자열 a 에서 i의 위치 찾기 (2가지 방법) ★★★★★
index_a = a.index('i') # i 없을 경우 오류 발생
print(index_a)
-> 작년 IM기출

find_a = a.find('i') # i 없을 경우 -1 반환
print(find_a)

# 3. 문자열 a의 문자 사이에 . 점 삽입 ★★
dot_a = '.'.join(a)
print(dot_a)

# 4. 문자열 a를 공백 기준으로 분리하기 ★★★★★
split_a = a.split()
print(split_a)

# 5. 문자열 a에서 'makes'를 'made'로 바꾸기
made_a = a.replace('makes','made')
print(made_a)

# 6. 문자열 a를 대문자에서 소문자로 바꾸기, 소문자에서 대문자로 바꾸기
print(a.lower())
print(a.upper())
print(a.swapcase())

# 7. 문자열 a의 양쪽 공백 삭제하기
strip_a = a.strip()
print(strip_a)

# 8. 입력된 시간(14:43:20) 에서 시간만 출력하기 ★★★★★
a = input().split(':')
print(a[0])

# 8-1 주민등록번호(890927-1212121) 에서 생일만 보여주기 / 성별보여주기

a = input().split('-')
# print(a[0][2:]) # 생일 : 0927

if a[1][0] == ('1' or '3'):
    print('남성')
elif a[1][0] == ('2' or '4'):
    print('여성')
else: 
    print('잘못된 값입니다.')
    
'''
# # 리스트 메서드 실습

# a = ['b', 'a', 'n', 'a', 'n']

# # 1. 리스트 a 의 마지막에 'a' 추가하기
# a.append('a')
# print(a)

# # 2-1. 리스트 a를 오름차순으로 정렬 (원본변경O)
# a.sort()
# print(a)

# # 2-2. 리스트 a를 오름차순으로 정렬 (원본변경X)
# a = ['b', 'a', 'n', 'a', 'n', 'a']

# # 3. 리스트 a를 내림차순으로 정렬
# a.sort(reverse=True)
# print(a)

# # 4. 리스트 a를 역순으로 뒤집기
# a = ['b', 'a', 'n', 'a', 'n', 'a']
# a.reverse()
# print(a)


# # 5. 리스트 a 에서 문자 'a'삭제하기
# num = a.count('a')
# for i in range(num):
#     a.remove('a')
# print(a)

# #########################################################
# # 2-2. 리스트 a를 오름차순으로 정렬 (원본변경X)
# a = ['b', 'a', 'n', 'a', 'n', 'a']
# print(sorted(a))    # ['a', 'a', 'a', 'b', 'n', 'n']
# print(a)    # ['b', 'a', 'n', 'a', 'n', 'a']

# # 6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 반환값 출력
# a = ['b', 'a', 'n', 'a', 'n', 'a']
# print(a.pop())

# # 7. 리스트 a에서 문자 'n'의 개수 출력
# a = ['b', 'a', 'n', 'a', 'n', 'a']
# print(a.count('n'))

'''
# 복사 : 할당 / 얕은복사 / 깊은복사
불변 데이터에는 문제가 없다. 가변 데이터일 때 원본이 변경될 수 있다.
원본 변경이 확실히 안 되는 것 : 깊은복사
'''
# 1. 할당
list1 = [1, 2, 3, 4]
list2 = list1

print(id(list1), id(list2)) # 메모리 주소 : id 
# 출력: 1903142670592 1903142670592 (메모리 주소가 같다.)

list2[0] = 5    # list2 값만 변경한다.
print(list1, list2) # 원본값도 함께 변경됨
# 출력: [5, 2, 3, 4] [5, 2, 3, 4]



# 2. 얕은 복사 : 객체 안에 객체가 있는 경우 원본 변경
list1 = [1, 2, [3, 4]]
list2 = list1.copy()

print(id(list1), id(list2))
# 출력 : 2622502904704 2622502904576 (메모리 주소가 다르다.)

print(id(list1[2]), id(list2[2])) # 2차원 리스트일 경우
# 출력 : 2346263750144 2346263750144 (메모리 주소가 같다.)



# 3. 깊은 복사 : 복사본이 변경되어도 원본 변경 X
import copy
list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)

print(id(list1), id(list2)) 
# 출력: 2973589283776 2973589283648 (메모리 주소 다르다.)

print(id(list1[2]), id(list2[2]))
# 출력 : 2973589383680 2973589286592 (메모리 주소 다르다.)