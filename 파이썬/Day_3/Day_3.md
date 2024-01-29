# ★함수 (중요!!)

특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

### 함수를 쓰는이유

두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드 중복 방지

**→ 재사용성 높아지고, 코드의 가독성, 유지보수성 향상**

```python
num1 = 5
num2 = 3
def get_sum(num1, num2):    # 두 수의 합 구하는 함수
    return num1 + num2
sum_result = get_sum(num1, num2)    # 함수 사용
print(sum_result)
```

### 내장 함수

파이썬이 기본적으로 제공 **(import 필요없음)**

*Ex) **print() // abs() : 절대값을 만드는 함수 //*** 

→ 외장함수 라는 말은 없다.

### 함수 호출

***functioin_name(arguments)***

함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드블록을 실행하는 것

### 함수의 구조

```python
def get_sum(num1, num2):    # INPUT
    '''이 함수는 두 수를 받아           # Docstring
    두 수의 합을 반환하는 함수입니다.

    >>>get_sum(1, 2)
    3
    '''
    return num1 + num2  # OUTPUT
```

### 함수의 정의와 호출

- 함수 정의
    - def 키워드로 시작
    - def 키워드 이후 함수 이름 작성
    - 괄호 안에 매개변수 정의 가능
    - 매개변수는 함수에 전달되는 값을 나타냄
- 함수 반환 값
    - **필요한 경우** 결과를 반환할 수 있음
    - return 키워드 이후에 반환할 값 명시
    - return 문은 함수의 **실행 종료** → 호출부분으로 반환

```python
# 함수 정의
def greet(name):    # 매개변수
    '''입력된 이름 값에
    인사를 하는 메세지를 만드는 함수
    '''
    message = 'hello' + name
    return message    # 종료 조건

# 함수 호출
result = greet('Alice')   # Argument
print(result)
```

- 함수 호출
    - 함수를 호출하기 위해서는 함수의 이름과 필요한 인자(Argument)를 전달해야함
    - 호출시 전달된 인자는 정의시 작성한 매개변수에 대입됨

### 매개변수와 인자

- 매개변수 : 함수를 **정의할 때** 함수가 받을 값을 나타내는 변수
- 인자 : 함수를 **호출할 때** 실제로 전달되는 값

```python
# 함수 정의
def add_numbers(x, y):   # x, y 는 매개변수 (반드시 2개의 인자만 받을 수 있다.)
    result = x + y
    return result    # return 이 필수는 아님.

# 함수 호출
a = 2
b = 3
sum_result = add_numbers(a,b)    # a, b는 인자
print(sum_result)
```

# 인자의 종류

### 위치 인자 ***Positional Arguments***

함수 호출시 인자의 위치에 따라 전달되는 인자

**★ 함수 호출시 반드시 값을 전달해야 함.**

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살 이시군요!')

greet('Alice', 25)    # 안녕하세요, Alice님! 25살 이시군요!
greet('Bella')    
# TypeError: greet() missing 1 required positional argument: 'age'
# -> 필수 위치 인자가 누락되었다.
greet("Alice", 20, 30)
# TypeError: greet() takes 2 positional arguments but 3 were given
```

### 기본 인자값

- 함수 **정의에서** 매개변수에 기본 값을 할당하는 것
- 함수 호출시 인자를 전달하지 않으면, 기본 값이 매개변수에 할당됨
    
    ```python
    def greet(name, age=30):
        print(f'안녕하세요, {name}님! {age}살 이시군요!')
    
    greet("Alice")    # 안녕하세요, Alice님! 30살 이시군요!   # 입력X -> 기본인자
    greet('Alice', 25)    # 안녕하세요, Alice님! 25살 이시군요! 
    # 입력하면 자동으로 배제된다.
    ```
    

### 키워드 인자

- 함수 **호출시** 인자의 이름과 함께 값을 전달 (정의시X)
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며 인자의 이름을 명시하여 전달
    
    ★ 단, 호출시 키워드 인자는 위치 인자 뒤에 위치해야 함
    
    ```python
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살 이시군요!')
    
    greet(age= 35, name = "Alice")    # 안녕하세요, Alice님! 35살 이시군요!
    greet(age = 35, 'Dave')    # 에러 발생
    # 위치인자 다음에 키워드인자를 써야함
    ```
    

### 임의의 인자 목록

- 정해지지 않은 개수의 인자를 처리하는 인자 (개수의 상관 없이)
- 함수 정의 시 매개변수 앞에 *를 붙여 사용하며, 여러개의 인자를 Tuple로 처리

```python
def calculate_sum(*args):    # 0개 이상 임의의 개수 처리한다는 뜻
    print(args)
    total = sum(args)
    print(f'합계: {total}')

calculate_sum(1, 2, 3)
"""
(1, 2, 3)   # 1개의 Tuple로 처리한다. -> Packing (값 변경 불가)
합계: 6
"""
```

### 임의의 **키워드 인자** 목록

- 정해지지 않은 개수의 키워드 인자를 처리하는 인자 (0개 이상)
- 함수 정의 시 매개변수 앞에  ** 를 붙여 사용하며, 여러개의 인자를 **dictionary로 묶어서** 처리

```python
def print_info(**kwargs):
    print(kwargs)

print_info(name = 'Eve', age = 30)
# {'name': 'Eve', 'age': 30}  -> dictionary
```

### 함수 인자 권장 작성 순서

**위치 → 기본 → 가변 → 가변 키워드**

- 호출시 인자를 전달하는 과정에서 혼란 줄일 수 있음
    
    *★단, 모든 상황에 적용되진 않음*
    

```python
def func(pos1, pos2, age=30, *args, **kwargs):
    print(pos1, pos2, age, args, kwargs)
    
func(1, 2, 3, 4, 5)    # 1 2 3 (4, 5) {}
func(1, 2, 3, a=100, b=200) # 1 2 3 () {'a': 100, 'b': 200}
```

---

# 함수와 Scope(공간)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable
    - global variable : global scope에 정의된 변수 → 전역 변수
    - local variable : local scope에 정의된 변수 → 지역 변수

### Scope예시

- num 은 로컬에 있어서 글로벌에서 못 씀
- 이는 변수의 수명주기와 연관이 있음.

### 변수의 수명주기

변수가 선언되는 위치와 스코프에 따라 결정

1. buit-in scope
    
    → 파이썬이 실행된 이후부터 영원히 유지
    
2. global scope
    
    → 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    
3. local scope
    
    → 함수가 호출될 때 생성되고 함수가 종료될 때까지 유지
    

```python
def func():
    num = 20
    print('local', num) # local 20
func()    # 여기서 num 변수가 죽음
print('global', num)    # num이 정의되지 않았다고 뜸
```

### 이름 검색 규칙

- 파이썬에서 사용되는 이름은 특정한 이름공간에 저장되어있음

- 다음 순서대로 이름을 찾아 나가며 LEGB Rule이라고 함
    1. Local scope
    2. Enclosed scope
    3. Global scope
    4. Built-in scope

```python
sum = 5    # 로컬에 sum 변수에 5 할당
print(sum)    # 5
print(sum(range(3)))    # 에러

# 빌트인 순위가 마지막 순위이기 때문에 
# sum 함수를 못 쓰게 됨
```

- 단, 역방향 X

```python
a = 1
b = 2

def enclosed():
    a = 10
    c = 3
    
    def local(c):    # 정의
        print(a, b, c)  # 10 2 500(호출될때 사용되므로)

    local(500)  # 호출 -> 여기서 사용 (매개변수 500)
    print(a, b, c)   # 10 2 3 -> enclosed함수

enclosed()
print(a, b) # 1 2 -> Global영역
```

### Global 키워드

- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
    
    ★주의사항
    
    - Global 키워드 선언 전에 접근 X
    - 매개변수에 Global 사용 X
- global 키워드는 가급적 사용하지 않는 것을 권장
- 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 함수의 반환값을 사용하는 것을 권장

## 재귀 함수

함수 내부에서 자기 자신을 호출하는 함수 ***(알고리즘 할 때 본격적으로 배움)***

1. 특징
    1. 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어듦. 가독성 높아짐
    2. 1개 이상의 base case (종료되는 상황) 가 존재하고 수렴하도록 작성 → 무한루프 방지
2. 예시 (팩토리얼)
    - n! = n * (n-1)! = n * n(-1) * (n-2)! = …
    - f(4) = 4 * f(3) // f(3) = 3 * f(2) // f(2) = 2* f(1) // f(1) = 1 (base case)
        
        → 주로 큰 것이 작은 것으로 줄어들 때 사용
        

```python
def factorial(n):
    # 종료조건
    if n == 0:
        return 1
    # 재귀호출
    return n * factorial(n-1)   # 자기 자신 호출

#계산 예시
result = factorial(5)
print(result)
```

→ 주의 사항 : 종료 조건 필수 ! (그렇지 않으면 무한 루프에 빠짐)

---

# 유용한 함수

## 내장 함수

### 1 ) map 과 zip 함수

- map(**function,** iterable)
    
    반복 가능한 데이터 구조(iterable) 의 모든 요소에 함수를 적용하고 그 결과를 map object로 반환
    
    ```python
    numbers = [1, 2, 3]
    result = map(str, numbers) # 함수의 이름만 쓴다.
    print(result)   # <map object at 0x0000021BEA5E4460> -> 맵 객체
    print(list(result))     # ['1', '2', '3'] -> 쓰고자 하는 데이터로 변환해야 함
    
    # 자주 쓰는 방법 -> 인풋을 여러개의 정수로 받기.
    numbers = input().split()
    result = map(int, numbers) # map 객체로 생성
    list_result = list(result) # int를 가진 list로 생성
    print(list_result)
    
    result = list(map(int, input().split())) # 한 줄로 작성하기
    ```
    

- zip (*iterables: 가변인자 + 반복가능)
    
    임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
    
    ```python
    girls = ['Jane', 'Ashely']
    boys = ['peter', 'jay']
    pair = zip(girls, boys)
    
    print(pair)
    print(list(pair))   # [('Jane', 'peter'), ('Ashely', 'jay')]
    # 쌍이 안 맞는다면 맞는데 까지만 출력
    ```
    

### 2) lambda 함수 : 익명 함수

- 구조
    - lambda 매개변수: 표현식
    - 람다 키워드 + 매개변수 + 표현식
- 간단한 연산이나 함수를 **한 줄로 표현할 때 사용**
- 함수를 매개변수로 전달하는 경우에도 유용하게 사용

```python
numbers = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

result = list(map(func, numbers)) 
print(result)

	result2 = list(map(lambda x: x **2, numbers))    # 재활용X
print(result2)
```

---

# Packing & Unpacking

## 1. Packing

- 여러개의 값을 하나의 변수에 묶어서 담는 것
- * 를 활용한 패킹
    
    ```python
    numbers = [1, 2, 3, 4, 5]
    a, *b, c = numbers
    
    print(a)    # 1
    print(b)    # [2, 3, 4] -> 남는 요소들을 리스트로 패킹
    print(c)    # 5
    ```
    

### 2. Unpacking

- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
- 튜플, 리스트 등의 객체의 요소들을 개별 변수에 할당
    
    ```python
    packed_values = 1, 2, 3, 4, 5
    a, b, c, d, e = packed_values
    
    print(a, b, c, d, e)
    # 개수가 다르면 unpacking 안 된다
    ```
    
- * 을 활용한 언패킹
    
    ```python
    names = ['alice', 'jane', 'peter']
    print(names)    # ['alice', 'jane', 'peter']
    print(*names)   # alice jane peter
    ```
    
- **를 활용한 언패킹
    
    ```python
    def my_function(key1, key2, key3):
        print(key1, key2, key3)
    
    my_dict = {'key1': 1, 'key2': 2, 'key3': 3}
    my_function(**my_dict)  # 1 2 3
    
    # key 이름과 매개변수 이름이 같아야 함
    # 개수도 같아야 함
    ```
    

### * , ** 패킹/ 언패킹 연산자 정리

- *
    - 패킹 연산자로 사용될 때, 여러개의 인자를 하나의 튜플로 묶는 역할
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹 하여 함수의 인자로 전달
- **
    - 패킹X
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 키워드 인자로 언패킹하여 함수의 인자로 전달하는 역할