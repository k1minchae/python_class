# 1/22(월)

# 1. 데이터 구조

- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 (str, list, dict ,…)
- 컴퓨터 공학에서는 ‘자료구조’라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠둔 것
- 각 데이터 구조의 **메서드**를 호출하여 다양한 기능 활용하기
    
    → 7, 8일차에 할 것
    

## 1) 메서드

- 객체(클래스) 에 속한 **함수**
- 객체의 상태를 조작하거나 동작을 수행
1. **특징**
    1. method 는 클래스 내부에 정의되는 함수
    2. 클래스는 파이썬에서 ‘타입을 표현하는 법’ → 이미 은연중에 씀
    3. help 함수를 통해 str을 호출해보면 class였다는 것을 확인 가능.
        
        ```python
        print(type('1')) # <class 'str'>
        ```
        
    
    **→ 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재**
    
    예시: list.append() → 리스트의 마지막에 객체를 추가하는 것.
    
    ```python
    def append():
        pass
    
    append()    # 함수 호출
    
    my_list = []
    my_list.append()    # 메서드 호출 
    # 객체.메서드() -> 데이터 타입의 객체가 호출함.
    
    print('hello'.capitalize())    # Hello
    ```
    

---

# 2. 시퀀스 데이터 구조

### 1. 문자열 탐색



```python
my_str = 'banana'

# find
print(my_str.find('a')) # a의 첫번째 위치(인덱스)를 반환
print(my_str.find('z')) # 없으면 -1을 반환

# index
print(my_str.index('a')) # a의 첫번째 인덱스 반환
print(my_str.index('z')) # ValueError: substring not found

# isalpha : 알파벳 문자로 이루어져있는지 ?
string1 = 'Hello'
string2 = '12a3'
print(string1.isalpha())    # True
print(string2.isalpha())    # False

# isupper -> 모두 대문자로 이루어져있는지 ?
# islower -> 모두 소문자로 이루어져있는지 ?
```

### 2. 문자열 조작 (새로운 문자열 반환)

***왜 원본을 변경하지 않을까?*** → 문자열은 ‘불변’ 데이터 타입이기 때문



1. ***.replace(old, new[,count])***
    
    ```
    text = 'Hello, world!'
    new_text = text.replace('world', 'python')
    print(new_text) # Hello, python!
    ```
    
    → 대괄호의 의미는 선택적으로 넣을 수 있다는 뜻 = **선택 인자**
    
    → 다른 언어에서도 공식 문서에서는 이 표기법을 씀 : 
    
    ***확장된 베커스 나우르 표기법***
    
    → 파이썬 EDNF 라고 검색하면 공식문서가 나온다.
    
2. ***.strip([chars])***
    
    문자열의 시작과 끝에있는 공백 혹은 지정한 문자를 제거
    
    ```python
    text = '  Hello, world!  '
    new_text = text.strip()
    print(new_text) # Hello, world!
    ```
    
3. ***.split(sep = None, maxsplit=-1)***
    
    ```python
    text = 'Hello, world!'
    new_text = text.split(',') # , 를 기준으로 나눔
    print(new_text) # ['Hello', ' world!']
    ```
    
4. ***‘separator(구분자)’.join(iterable(반복가능한)) ↔ split***
    
    ```python
    # split (쪼개기)
    text = 'Hello, world!'
    new_text = text.split(',')
    print(new_text) # ['Hello', ' world!']
    
    # join (합치기)
    words = ['Hello', 'world!']
    text= '-'.join(words)   # -를 기준으로 두 문자를 합침
    print(text) # 'Hello-world!
    ```
    
5. **문자열 조작 메서드**
    

    

**★ 메서드는 이어서 사용 가능하다.**



**→ 단, 앞쪽에 메서드의 반환값이 (None) 이라면 이어갈 수 없음!**

### 3. List 값 추가 및 삭제 메서드 ★

→ **새로운 값에 할당하지 않고 원본 값을 수정함**

***print(my_list.append(1)) → None***

1. .***append(x) :*** 리스트 마지막에 항목 x추가
2. ***.extend(iterable) :*** 리스트 끝에 iterable 객체의 모든 항목을 추가
    
    ```python
    # append
    my_list.append(4)
    my_list.append([5, 6, 7])   # 이건 풀려서 안들어감
    print(my_list)
    
    # .extend
    my_list.extend([5, 6, 7])   # iterable 한 요소가 풀려서 들어감
    print(my_list)
    ```
    
3. .insert(i, x) : 리스트의 지정한 인덱스 위치에 항목 x 삽입
    
    ```python
    my_list = [1, 2, 3, 4, 5]
    # insert
    my_list.insert(3, 'ssafy')  # 인덱스 3에 'ssafy' 추가
    print(my_list)
    ```
    
4. .remove(x) : 리스트에서 첫번째로 일치하는 항목 삭제
5. ★ ***.pop(i)*** : 리스트에서 지정한 인덱스의 항목 제거 + **제거한것 반환**
    
    지정하지 않을 경우 마지막 항목 제거
    
    반환하기 때문에 **return 값이 존재한다. → 변수에 할당 가능**
    
    ```python
    # pop
    my_list = [1, 2, 3, 4, 5]
    item1 = my_list.pop()
    print(item1)    # 마지막 값 제거(5) + 반환
    
    item2 = my_list.pop(0)
    print(item2)    # 0번 인덱스 값(1) 제거
    
    print(my_list)  # 마지막 값과 0번째 값이 제거된 상태로 출력
    ```
    
6. .clear() : 리스트의 모든 항목 삭제

### 4. 리스트 탐색 및 정렬 메서드

1. ***L.index(x, start, end)*** : (범위 내에서 가장 왼쪽에있는 x**반환**)
    
    문자열의 .find(x) 와 유사함
    
    ```python
    # index
    my_list = [1, 2, 3, 3, 3]
    index = my_list.index(3) # return 값이 있어서 변수에 할당 가능
    print(index) # 2
    ```
    
2. ***L.reverse()*** : 리스트의 순서를 역순으로 변경 (정렬X)
    
    ```python
    my_list = [1, 3, 2, 8, 1, 9]
    my_list.reverse()
    print(my_list)  # [9, 1, 8, 2, 3, 1]
    # 이것도 역시 반환값 X
    ```
    
3. ***L.sort()*** : 리스트를 정렬 (매개변수 이용가능) → **반환값 None**
    
    ```python
    my_list = [3, 2, 1]
    
    # 기본값: 오름차순
    sorted_list = my_list.sort()    
    print(sorted_list)  # None (반환값 X)
    print(my_list) # [1, 2, 3] 원본 값을 바꿔주기 때문.
    
    my_list.sort(reverse=True) # 내림차순
    # .sort() 는 sort(reverse=False) 상태임.
    print(my_list)  # [3, 2, 1]
    ```
    
4. ***L.count(x)*** : 리스트에서 항목x의 개수를 반환
    
    ```python
    # count
    my_list = [1, 2, 3, 3, 3]
    count = my_list.count(3)
    print(count)    # 3
    ```
    

---

# 3. 복사

### 1. 데이터 타입과 복사

- 파이썬에서는 데이터 분류에 따라 복사가 달라짐
- **변경가능한 데이터 타입**과, **변경 불가능한 데이터 타입**을 달리 다룸

```python
# 변경 가능한 데이터
a = [1, 2, 3, 4]
b = a   # a, b 의 주소값이 같다. -> 할당
b[0] = 100 

print(a) # a도 바꼈을까? -> 같이 바뀜. [100, 2, 3, 4]
print(b) # b의 값은 당연히 바뀜 [100, 2, 3, 4]

# 변경 불가능한 데이터
a = 100
b = a

b = 9    # 재할당
print(a)    # 100 (안바뀜!★) -> 변경 불가능한 데이터
print(b)    # 9
```

### 2. 복사의 유형

1. **할당**
    
    ```python
    # 리스트 복사 예시 
    original_list = [1, 2, 3]
    copy_list = original_list # 할당 (주소값이 같다.)
    # 할당연산자(=)를 통한 복사는 객체 참조값을 복사
    
    copy_list[0] = 'hello'
    print(original_list)    # ['hello', 2, 3] (원본도 바뀜)
    ```
    

2. **얕은 복사** : slicing 활용

```python
# slicing : 자른 뒤 '새로운'리스트를 만듦 (주소값 달라짐)
a = [1, 2, 3]   
b = a[:]
b[0] = 100

print(a)    # 원본값이 바뀌지 않음
```

**★ 얕은 복사의 한계**

- 2차원 리스트와 같이 변경 가능한 객체안에 또 변경가능한 객체가 있는 경우 → **안쪽에 있는 리스트는 복사 X**

```python
a = [1, 2, [1, 2]]
b = a[:]

b[2][0] = 100
print(a) # [1, 2, [100, 2]] -> 2차원 리스트는 안 됨
```

1. **깊은복사 :** 모듈 활용  (copy.deepcopy)
    
    ```python
    import copy
    
    original_list = [1, 2, [3, 4]]
    deep_copied_list = copy.deepcopy(original_list) 
    # deepcopy 함수 활용 -> 모습만 같고 아예 다른 list가 됨
    
    deep_copied_list[2][0] = 100
    
    print(original_list) # [1, 2, [3, 4]] 
    # 2차원 리스트임에도 원본은 바뀌지 않음
    ```
    
- 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참고하게 함

---

# 참고

### 문자열에 포함된 문자들의 유형을 판별하는 메서드

- **isdecimal()**
    
    문자열이 모두 숫자 문자로만 이루어져있어야 True
    
- **indigit()**
    
    유니코드 숫자도 숫자로 인식 ③ ← 이런거
    
- **isnumeric()**
    
    isdigit() 과 유사하지만, 몇 가지 추가적인 유니코드 문자 인식
    
    (분수, 지수, 루트 기호 등)


**→ 외울 필요는 없다.**

---

# 실습

### 문자열 메서드 실습

- 문자열은 불변시퀀스라서 원본 안 바뀜.
- 구조 : 객체.method

```python
a = ' Practice makes perfect '
# 1. 문자열 a 에서 e의 개수 세기 ★★★
count_e = a.count('e')
print(count_e)

# 2. 문자열 a 에서 i의 위치 찾기 (2가지 방법) ★★★★★
# 작년 IM 기출
index_a = a.index('i') # i 없을 경우 오류 발생
print(index_a)

find_a = a.find('i') # i 없을 경우 -1 반환
print(find_a)

# 3. 문자열 a의 문자 사이에 . 점 삽입 ★★
dot_a = '.'.join(a)
print(dot_a)

# 4. 문자열 a를 공백 기준으로 분리하기 ★★★★★
split_a = a.split()
print(split_a)

# 5. 문자열 a에서 'makes'를 'made'로 바꾸기
# 원본은 변경되지 않는다.
made_a = a.replace('makes','made')
print(made_a)

# 6. 문자열 a를 대문자에서 소문자로 바꾸기, 소문자에서 대문자로 바꾸기
print(a.lower())
print(a.upper())
print(a.swapcase())

# 7. 문자열 a의 양쪽 공백 삭제하기
strip_a = a.strip()
print(strip_a) # Practice makes perfect

# 8. 입력된 시간(14:43:20) 에서 시간만 출력하기 ★★★★★
a = input().split(':')
print(a[0]) # 14

# 8-1 주민등록번호(890927-1212121) 에서 생일만 보여주기 / 성별보여주기
a = input().split('-')
# print(a[0][2:]) # 생일 : 0927

if a[1][0] == ('1' or '3'):
    print('남성')
elif a[1][0] == ('2' or '4'):
    print('여성')
else: 
    print('잘못된 값입니다.')
```

### 리스트 메서드 실습

```python
# 반환하지 않는 메서드 : 주로 원본 변경
# 1. 리스트 a 의 마지막에 'a' 추가하기 ★★★★★
	# stack(후입선출) 에서 많이 사용됨. + pop
a = ['b', 'a', 'n', 'a', 'n']
a.append('a')
print(a)

# 2-1. 리스트 a를 오름차순으로 정렬 (원본변경O)
a.sort()
print(a)

# 2-2. 리스트 a를 오름차순으로 정렬 (원본변경X)
a = ['b', 'a', 'n', 'a', 'n', 'a']
# 반환하는 메서드에 입력.

# 3. 리스트 a를 내림차순으로 정렬
a.sort(reverse=True)
print(a)

# 4. 리스트 a를 역순으로 뒤집기
a = ['b', 'a', 'n', 'a', 'n', 'a']
a.reverse()
print(a)

# 5. 리스트 a 에서 문자 'a'삭제하기
num = a.count('a')
for i in range(num):
    a.remove('a')
print(a)

#############################################################
# 반환하는 메서드 : 주로 원본 변경 X
# 2-2. 리스트 a를 오름차순으로 정렬 (원본변경X) ★★★
a = ['b', 'a', 'n', 'a', 'n', 'a']
print(sorted(a))    # ['a', 'a', 'a', 'b', 'n', 'n']
print(a)    # ['b', 'a', 'n', 'a', 'n', 'a']

# 6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 반환값 출력
a = ['b', 'a', 'n', 'a', 'n', 'a']
print(a.pop()) # 오히려 remove 보다 pop많이 씀

# 7. 리스트 a에서 문자 'n'의 개수 출력
a = ['b', 'a', 'n', 'a', 'n', 'a']
print(a.count('n'))
```

### 복사

- 할당 / 얕은복사 / 깊은복사
- 불변 데이터에는 문제가 없다.
- 가변 데이터일 때 원본이 함께 변경될 수 있다.
- 확실히 원본 변경이 안되는 것 : 깊은복사

```python
# 1. 할당 : 원본 변경 O
list1 = [1, 2, 3, 4]
list2 = list1

print(id(list1), id(list2)) # 메모리 주소 : id 
# 출력: 1903142670592 1903142670592 (메모리 주소가 같다.)

list2[0] = 5    # list2 값만 변경한다.
print(list1, list2) # 원본값도 함께 변경됨
# 출력: [5, 2, 3, 4] [5, 2, 3, 4]

----------------------------------------------------------

# 2. 얕은 복사 : 객체 안에 객체가 있는 경우 원본 변경
list1 = [1, 2, [3, 4]]
list2 = list1.copy()

print(id(list1), id(list2))
# 출력 : 2622502904704 2622502904576 (메모리 주소가 다르다.)

print(id(list1[2]), id(list2[2])) # 2차원 리스트일 경우
# 출력 : 2346263750144 2346263750144 (메모리 주소가 같다.)

----------------------------------------------------------

# 3. 깊은 복사 : 복사본이 변경되어도 원본 변경 X
import copy
list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)

print(id(list1), id(list2)) 
# 출력: 2973589283776 2973589283648 (메모리 주소 다르다.)

print(id(list1[2]), id(list2[2]))
# 출력 : 2973589383680 2973589286592 (메모리 주소 다르다.)
```