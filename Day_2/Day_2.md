# [Sequence Type] : list, tuple, range

# list

여러개의 값을 순서대로 저장하는 ***변경 가능한*** 시퀀스 자료형

### 리스트 표현

- 0개 이상의 객체를 포함하며 데이터 목록을 저장
- 대괄호 [] 로 표기
- 데이터는 어떤 자료형도 저장할 수 있음 (리스트 안에 리스트 저장OK)

```python
my_list_1 = []    # 빈 리스트
my_list_2 = [1, 'a', 3, 'b', 5]    # 문자열도 저장 가능
my_list_3 = [1, 2, 3, ['hello', 'world', '!!!']]    # 리스트 안에 리스트 가능
```

### 리스트의 시퀀스 특징 (=Tuple)

- 인덱싱
- 슬라이싱
- 길이

```python
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])    # a

# 슬라이싱
print(my_list[2:4])    # [1, 'a', 3]

# 길이
print(len(my_list))    # 5
```

### 중첩된 리스트 접근

출력값 예상해보기

```python
my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']]

print(len(my_list)) = 5
print(my_list[4][-1]) = '!!!'    # ['hello, 'world', '!!!'] 에서 -1번째 인덱스
print(my_list[-1][1][0]) = 'w'['hello', 'world', '!!!']->'world'-> 'w'
```

### 리스트의 가변성

```python
my_list = [1, 2, 3]
my_list[0] = 100
my_list = [100, 2, 3]
```

---

# Tuple

여러 개의 값을 순서대로 저장하는 ***변경 불가능 한*** 시퀀스 자료형

### 튜플 표현

- 0개 이상의 객체를 포함하여 데이터 목록을 저장 (=리스트)
- 소괄호로 표기
- 데이터는 어떠한 자료형도 저장할 수 있음 (=리스트)

```python
my_tuple_1 = ()

#요소가 하나인 Tuple 은 ,가 필수이다.
my_tuple_2 = (1,)    # , 가 없으면 정수가 되어서 소괄호가 사라져버림

my_tuple_3 = (1, 'a', 3, 'b', 5)
```

### 튜플의 불변성

```python
my_tuple = (1, 'a', 3, 'b', 5)

my_tuple[1] = 'z'

# TypeError : 'tuple' object does not support item assignment
```

- 튜플의 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당
- 개발자가 직접 사용하기보다 파이썬 내부동작에서 주로 사용된다.

```python
x, y = (10, 20)    # 파이썬 내부에서 튜플로 처리가 된다.
print(x)
print(y)

# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호 생략 가능
x, y = 10, 20    # 자동으로 튜플로 처리함
```

---

# Range

연속된 정수 시퀀스를 **생성하는** 변경 불가능한 자료형

- range(n) : 0부터 n-1 까지의 숫자 시퀀스
- range(n, m) : n부터 m-1 까지의 숫자 시퀀스

**→ 출력 결과를 보면, 숫자로 바로 출력되지 않는다. (변경도 X)**

```python
my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1)    # range(0, 5)
print(my_range_2)    # range(1, 10)
```

### range 표현

- 리스트로 형 변환 시 데이터 확인 가능
- 주로 반복문과 함께 사용한다

```python
print(list(my_range_1))    # [0, 1, 2, 3, 4]
print(list(my_range_2))    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

# [Non-sequence Type] : Dict, Set

# Dict

딕셔너리 : **key - value** 의 쌍으로 이루어진

**순서와 중복이 없는** (시퀀스와의 차이) 변경가능한 자료형

### 딕셔너리 표현

- key 는 변경 불가능한 자료형만 사용 가능 (문자, 정수, 실수, 튜플, range)
- value는 모든 자료형 사용 가능
- 중괄호로 표기 (=set)

```python
my_dict_1 = {}
my_dict_2 = {'key': 'value'}    # key : value 한 쌍당 값이 1개
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_1)    # {}
print(my_dict_2)    # {'key': 'value'}
print(my_dict_3)    # {'apple': 12, 'list': [1, 2, 3]}
```

### 딕셔너리 사용

- **key 를 통해 value에 접근**
- 순서가 없기 때문에 index가 없다
- **중복이 없다**

```python
my_dict = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict[2]) ≠ {‘list’: [1, 2, 3]}    # 순서가 없어서 index가 없음

print(my_dict['apple'])    # 12 // key 를 통해 값을 불러온다. (Index 사용X)
my_dict['apple'] = 100    # key 를 통해 value 변경 가능
print(my_dict)    # {'apple': 100, 'list': [1, 2, 3]}

my_dict = {
    'apple': 12,
    'list': [1, 2, 3],
    'apple': 100    # apple 이라는 요소 중복 (중복 불가)
}

print(my_dict)      # {'apple': 100, 'list': [1, 2, 3]}
                    # 중복되면 마지막 요소만 출력이 됨
```

---

# set

**순서와 중복이 없는** 변경 가능한 자료형 (dict 와 특징은 동일하지만 key: value쌍이 아님)

### 세트 표현

- 수학에서의 집합과 동일한 연산 처리 가능
- 중괄호로 표기 (dict)
- **빈 세트를 만들 때** set() 라는 내장함수를 사용하여 **my_set = set()** 로 만든다.
    
    → 빈 dict 랑 표현이 겹치면 안되므로. **my_dict = {}**
    

```python
my_set_1 = {1, 1, 1}    # 세트는 중복이 안 됨.
print(my_set_1) = {1}    # 그래서 하나만 출력이 된다.

my_set_2 = {1, 2, 3}
print(my_set_2[3]) # 세트는 순서가 없다.
```

### 집합 연산

```python
my_set_1 = {1, 2, 3}
my_set_2 = {3, 4, 5}

# 합집합 | (shift \)
print(my_set_1 | my_set_2)   # {1, 2, 3, 6, 9}

# 차집합 -
print(my_set_1 - my_set_2) # {1, 2}

# 교집합 &
print(my_set_1 & my_set_2) # {3}
```

---

# [기타 자료형]

# None

파이썬에서 ‘값이 없음’을 표현하는 자료형 (첫글자 : 대문자)

# Boolean

참(True)과 거짓(False)을 표현하는 자료형

### 불리언 표현

- 비교/ 논리 연산의 평가 결과로 사용됨
- 주로 조건/ 반복문과 함께 사용

```python
bool_1 = True    # True False의 첫 글자는 대문자로 써야함
bool_2 = False
print(bool_1)    # True
print(3 > 1)    # True
print('3' != 3)    # True
```

# Collection

sequence 와 non-sequence 의 공통점 : 여러개의 값 저장함 → collection

|  | 변경 가능 여부 | 순서 여부
(시퀀스/논시퀀스 구분) |
| --- | --- | --- |
| str | X | O |
| list | O | O |
| tuple | X | O |
| set | O | X |
| dict | O | X |

---

### 형 변환 (Type Conversion)

1. **암시적 형변환**
    
    → 파이썬이 자동으로 해 줌
    

```python
print(3 + 5.0)    # int 3을 float인 3.0 으로 바꿔서 8.0출력
print(True + 3)    # 4 (True 가 1로 변경됨)
print(True + False)    # 1 (False는 0 // True는 1)

# 그래도 이런 코드가 안 나오게 하는게 좋다.
```

1. **명시적 형변환**
    
    → 개발자가 직접 형변환을 하는 것. (대부분의 경우)
    

- str → integer : 형식에 맞는 숫자만 가능
- integer → str : 모두 가능

```python
print(int('1'))    # 1
print(int('3.5'))   # Error -> Float 이기 때문에 int로 변경 불가
print(float('3.5'))    # 3.5 (변경 가능)
# 문자를 numeric type으로 바꾸려면 형식에 맞아야 함.

print(int(3.5))    # 3
# numeric 간 형변환을 하면 형식에 맞게 버림 해줌.

print(str(1) + '등')    # 정수 1을 문자열로 바꾸고 '등' 문자열과 결합
# numeric -> str 은 모두 가능
```

---

# [연산자]

# 복합 연산자

연산과 할당이 함께 이루어짐 (축약형태)

| 기호 | 예시 | 의미 |
| --- | --- | --- |
| += | a += b | a = a + b |
| -= | a -= b | a = a - b |
| *= | a *= b | a = a * b |
| /= | a /= b | a = a / b |
| //= | a //= b | a = a // b |
| %= | a %= b | a = a % b |
| **= | a **= b | a = a ** b |

```python
y = 10
y -= 4
print(y)    # 6

# 10에서 4 를 뺀 결과를 재 할당
```

- 연산자를 먼저 쓰고 그 뒤에 부등호

# 비교 연산자

| 기호 | 내용 |
| --- | --- |
| < | 미만 |
| < = | 이하 |
| > | 초과 |
| > = | 이상 |
| == | 같음 |
| ! = | 같지 않음 |
| is | 같음 |
| is not | 같지 않음 |

- 부등호를 먼저 써야함
- 모든 결과는 Boolean 값

### is 비교 연산자

- 메모리 내에서 같은 객체를 참조하는지 확인 (주소 비교)
- == 는 동일성 (equality), is 는 식별성 (identity)
- is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용

```python
print(2.0 == 2)    # True
print(2.0 is 2)    # False

print(1==True)     
# True (암시적 형 변환으로 통과가 
#       되어서 디버깅이 힘듦)

print(1 is True)    
# False (메모리 주소가 다르기 때문)
```

### 논리 연산자

| 기호 | 연산자 | 내용 |
| --- | --- | --- |
| and | 논리곱 | 양쪽 피연산자가 모두 True 여야 True |
| or | 논리합 | 양쪽 피연산자 중 1개만 True 여도 True |
| not | 논리부정 | 단일 피연산자 부정 |

```python
# 비교 연산자와 함께 사용

num = 15
result = (num > 10) and 
(num % 2 == 0)

#10보다 큰 짝수 찾는 조건

print(result)   # False
```

★ ***단축 평가***

논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

→ Ex. False and ??? : 앞에 것만 봐도 이미 False 여서 뒤에를 안 봐도 됨

```python
vowels = 'aeiou'

print(('a' and 'b') in vowels)  # False (b -> b in vowels -> False)
print(('b' and 'a') in vowels)  # True  (a -> a in vowels -> True)
# 괄호 안에 꺼를 먼저 판단

print(3 and 5)  # 5 (둘다 True 면 뒤에꺼)
print(3 and 0)  # 0
print(0 and 3)  # 0 (0이 False -> 뒤에까지 평가 안 함) 
print(0 and 0)  # 0 

print(5 or 3)   # 5 (or 은 뒤에까지 다 봐야함)
print(3 or 0)   # 3
print(0 or 3)   # 3
print(0 or 0)   # 0
```

- and
    - 첫번째 피연산자가 False인 경우, 전체 표현식은 False로 결정
    - 두번째 피연산자는 평가되지 않고 그 값이 무시
    - 첫번째 피연산자가 True인 경우 전체 표현식의 결과는 두번째 피연산자에 의해 결정
    - 두번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
- or
    - 첫번째 피연산자가 True인 경우, 전체 표현식은 True로 결정
    - 두번째 피연산자는 평가되지 않고 그 값이 무시됨
    - 첫번째 피연산자가 False인 경우 전체 표현식의 결과는 두번째 피연산자에 의해 결정
    - 두번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환

### 멤버십 연산자

특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인

- in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인
- not in : 속하지 않는지를 확인

### 시퀀스형 연산자

- + : 결합연산자
- * : 반복 연산자
  
```
print('Gildong' + 'Hong')   #Gildong Hong
print('hi' * 5) # hihihihihi
print([1, 2] * 2) # [1, 2, 1, 2]
```

### 실습1

인덱싱하여 3을 출력해보세요.

### 실습2

인덱싱하여 7을 출력해보세요.

### 실습3

슬라이싱하여 [2, 3]을 출력해보세요.

```python
MAP = []
Matric = []
array = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]

print(array[0][2])    # 1번: 3

print(array[2][0])    # 2번: 7

print(array[0][1:3])    # 3번: [2, 3]
```