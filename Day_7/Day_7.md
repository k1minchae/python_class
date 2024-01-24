# [OOP]

<span style="color:red"># 1. 객체 지향 프로그래밍</span>

1. **절차 지향 프로그래밍**
    
    *c언어, 포트란, …*
    
    - 프로그램을 데이터와 절차로 구성하는 방식
    - 데이터와 함수가 분리되어 있다
    - 데이터와 함수(절차)가 분리되어 있으며 **순서/흐름**이 중요
    - 데이터 재사용 어려움
    
    **→ 소프트웨어 위기**
    
    - 하드웨어의 발전으로 복잡성, 용량 급증
    - 소프트웨어에 충격이 발생함

1. **객체 지향 프로그래밍**
    
    *파이썬, 자바, 자바스크립트, …*
    
    - 데이터와 해당 데이터를 조작하는 메서드(메시지)를 하나의 객체(클래스)로 묶어서 관리하는 방식
    - 객체간 상호작용과 메세지 전달이 중요


- 클래스를 통해 데이터의 상하관계 개념이 생김
- 절차 지향 : 공격(전사)  **** 함수 중심***
- 객체 지향 : 전사 → 베기  **** 객체 중심***

***★ 단, 절차지향과 객체지향은 서로 대조되는 것이 아니라, 객체지향은 기존의 절차지향 시스템을 기반으로 기존 절차지향을 보완하기 위해 ‘객체’라는 개념을 도입한 것***

### 클래스

파이썬에서 타입을 표현하는 방법 : **데이터 + 타입**

- 객체를 생성하기 위한 **설계도**
    
    (Ex. **클래스** : 가수 **→** **객체** : 아이유, BTS, …)
    
- 클래스를 통해 객체를 찍어낸다
    
    클래스로 만든 객체를 **인스턴스** 라고 함.
    
    - 아이유는 객체다 (O)
    - 아이유는 인스턴스다 (X)
    - 아이유는 가수의 인스턴스다 (O)
- 데이터와 기능을 함께 묶는 방법 제공
- **‘클래스를 만든다’ = 타입을 만든다**

### 객체

클래스에서 정의한 것을 토대로 메모리에 할당된 것

→ **속성(정보)**과 **행동(동작)**으로 구성된 모든 것

→ 속성 : 변수 // 행동 : 메서드

**→ 파이썬의 모든 것은 객체이다.**

→ 클래스, 함수마저도 객체임

### 객체의 특징

**객체 = 속성 + 기능**

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가 ?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가 ?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가 ?

### 클래스와 객체

```python
name = 'Alice'
print(type(name))   # <class 'str'>
```

- 변수 name의 타입은 str 클래스이다.
- 변수 name은 str 클래스의 **인스턴스**이다.
- 우리가 사용했던 데이터 타입은 사실 모두 클래스였다.
- type() 함수는 어떤 클래스에서 만들어졌는지를 보여줌

### 인스턴스와 메서드

- 클래스 안에 메서드가 들어가 있다.
- 같은 클래스 안에 들어있는 인스턴트만 해당 메서드를 사용 가능
- 인스턴스.메서드() 방식으로 사용함
    
    **→ 예시 : ‘hello’.upper()**
    
    → upper() 메서드는 str 클래스에 들어있다.
    
    → ‘hello’는 str 클래스의 인스턴스이다.
    

### 클래스 구조

- 클래스 정의
    
    ```python
    # PaskalCase 로 만들어야 함 (Style Guide)
    class Person:
        pass
    
    평소 함수를 만들 땐 snake_case로 만든다.
    ```
    

- 인스턴스 생성
- 메서드 호출
- 속성(변수) 접근

```python
# 인스턴스 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute
```

→ 클래스를 한 번 만들어두면 수많은 인스턴트에 재사용 가능해서 효율적이다.

→ 인스턴스는 같은 곳에서 만들어졌지만 각각 독립적임

### 클래스와 인스턴스 변수 생성

```python
# 클래스 정의
class Person:
    # 클래스 변수 (속성) -> 클래스 내부에 선언된 변수
    blood_color = 'red' # 클래스의 모든 인스턴스들이 '공유'하는 변수

    # 생성자 함수
    def __init__(self, name):  # self : 인스턴스 자기 자신
        self.name = name    # 인스턴스 변수 : 인스턴스마다 독립적인 값 (생성될때마다 초기화)
    '''
    - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
    - __init__ 이라는 이름의 메서드로 정의하며, 객체 초기화 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값 설정
    '''

    # 인스턴스 메서드
    def singing(self):  # 인스턴스가 쓸 수 있는 메서드
        return f'{self.name}가 노래합니다.'
    '''
    - 각각의 인스턴스에서 호출 가능한 메서드
    - 각각의 인스턴스 변수에 접근하고 수정가능
    '''

# 인스턴스 생성 -> __init__ 호출
singer1 = Person('IU')  
singer2 = Person('bts')

# 메서드를 호출
print(singer1.singing())    # IU가 노래합니다.
print(singer2.singing())    # bts가 노래합니다.

# 속성 접근
print(singer1.blood_color)  # red
print(singer2.blood_color)  # red
```



- 클래스를 정의하면 클래스와 해당 이름 공간 생성
- 인스턴스를 만들면 인스턴스 객체가 생성되고 독립적인 이름공간 생성
- 인스턴스에서 특정 속성에 접근하면, **인스턴스 → 클래스 순으로** 탐색

### 인스턴스와 클래스 간의 이름 공간

```python
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()   # unknown -> 클래스 변수에 접근

p2 = Person()
p2.name = 'Kim'
p2.talk()   # Kim -> 인스턴스 변수에 먼저 접근

print(Person.name)  # unknown

p2.ssafy = 11   # p2 는 p2안에 독립적 공간을 가져서 맘대로 생성 가능
print(p2.ssafy)
print(p1.ssafy) # AttributeError: 'Person' object has no attribute 'ssafy'
```

- **각 인스턴스는 독립적인 메모리 공간 가짐**
- 다른 클래스나 다른 인스턴스 간에는 서로 직접 접근 X
- 객체 지향 프로그래밍의 중요한 특성 중 하나
- 클래스와 인스턴스 모듈화 → 각각 독립적으로 동작 (서로 엉키지 X)
- 상호작용에서 서로 충돌X 영향X
- ***코드의 가독성, 유지보수성, 재사용성 높이는데 도움을 줌***

### 클래스 변수 활용

1. **가수가 몇명인지 확인하고 싶다면 ?** 
    
    ```python
    class Person:
            count = 0
            
            def __init__(self, name):
                self.name = name
                Person.count += 1
    		       # 인스턴스가 생성될 때 마다 변수가 + 1
            
            
        person1 = Person('iu')
        person2 = Person('BTS')
            
        print(Person.count)  # 2
    ```
    
2. **클래스 변수와 인스턴스 변수**
    
    ```python
    class Circle:
        pi = 3.14    # 클래스의 속성
    
        def __init__(self, r): # 생성자 함수
            self.r = r    # 인스턴스 변수에 변수 r 생성
    
        c1 = Circle(5)
        c2 = Circle(10)
        print(Circle.pi)  # 3.14
        print(c1.pi)  # 3.14
        print(c2.pi)  # 3.14 
        
     
    -----------------------------------------------------
        
        
        class Circle:
        pi = 3.14
    
        def __init__(self, r):
            self.r = r 
    
        c1 = Circle(5)
        c2 = Circle(10)
        Circle.pi = 5  # 클래스 변수 변경
        print(Circle.pi)  # 5
        print(c1.pi)  # 5
        print(c2.pi)  # 5 
     
    
    ------------------------------------------------------
    
        
        class Circle:
        pi = 3.14
    
        def __init__(self, r):
            self.r = r 
    
        c1 = Circle(5)
        c2 = Circle(10)
        c2.pi = 5  # 인스턴스 변수 변경
        print(Circle.pi)  # 3.14 (클래스 변수)
        print(c1.pi)  # 3.14 (클래스 변수)
        print(c2.pi)  # 5 (새로운 인스턴스 변수가 생성됨)
    ```
    

---

# 메서드의 종류

1. 인스턴스 메서드
2. 클래스 메서드
3. 정적 메서드

### 1. 인스턴스 메서드

클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

→ 인스턴스의 상태 조작 or 동작 수행

- 클래스 내부에 정의되는 메서드의 기본
- **반드시 첫 번째 매개변수로 인스턴스 자신을 전달받음 (self 필수★)**
    
    ```python
    # self 동작 원리
    
    # upper 메서드를 통해 대문자로 변경
    'hello'.upper() # 객체지향 방식 -> 단축형 호출
    
    # 파이썬 내부 동작
    str.upper('hello')
    # str 클래스가 upper 호출 -> 그 인자로 인스턴스 들어감
    
    ---
    
    class MyClass:
    
        def instance_method(self, arg1):    
    	                    # self 쓰고 그뒤에 추가인자 쓰면됨
                          # 이름이 꼭 self 가 아니어도 작동은 됨
            pass
    ```
    

### 생성자 메서드

인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

**→ 인스턴스 변수들의 초기값 설정**

```python
class Person:
	  # 생성자 메서드
    def __init__(self, name):
        print(f'{name} 인스턴스가 생성되었습니다.')

person1 = Person('지민') # 지민 인스턴스가 생성되었습니다.
```

### 클래스 메서드

클래스가 호출하는 메서드

→ 클래스 변수를 조작하거나 클래스 단위의 동작 수행

- **@classmethod 데코레이터 필수**
    
    ```python
    class MyClass:
    
        # 클래스 메서드는 데코레이터를 사용하여 정의
        @classmethod # <<내장 데코레이터 : 기능적으로 업그레이드 해줌 ??
        def class_method(cls, arg1):    # 첫번째가 꼭 cls여야 함 (이름은 약속)
            print(f'{name} 인스턴스가 생성되었습니다.')
    
    cls.class명 으로 접근함
    ```
    

- **클래스 메서드 예시**
    
    ```python
    class Person:
        count = 0
    
        def __init__(self, name):
            self.name = name
            Person.count += 1
    
        @classmethod
        def number_of_population(cls):
            print(f'인구수는 {cls.count}입니다.')
           # person.count(o) 
           # 하지만, 이렇게 하면 클래스 상속했을 때 문제 생김
    
    person1 = Person('iu')
    person2 = Person('BTS')
    
    Person.number_of_population() # 인구수는 2입니다.
    ```
    

### 스태틱(정적) 메서드

클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드

**→ 주로 클래스와 관련 있지만 인스턴스와 상호작용이 필요하지 않을 때**

- #staticmethod 데코레이터를 사용해서 정의
- 객체 상태나 클래스 상태 수정 X 단지 기능만을 위한 메서드
- 사용 : class.staticmethod() **(★ 클래스가 호출한다.)**

### 비교

1. **인스턴스 메서드** : 인스턴스의 상태변경, 인스턴스 동작수행
    
    → self 필수
    
2. **클래스 메서드** : 인스턴스의 상태에 의존 X, 클래스 변수 조작
    
    → @classmethod 와 cls 필수
    
3. **스태틱 메서드** : 클래스 , 인스턴스와 관련 없는 일반적 기능 수행
    
    → @staticmethod 필수
    
- 클래스가 사용해야할 것 : 클래스 메서드, 스태틱 메서드
- 인스턴스가 사용하는 것 : 인스턴스 메서드

**→ 클래스가 인스턴스 메서드를 사용하지 못 하는 건 아님!**

→ 인자에 인스턴스 넣어주면 되지만 그렇게 쓰지 않음.

★ 인스턴스도 모든 메서드 호출 가능

★ 클래스도 모든 메서드 호출 가능

***→ 하지만 그렇게 쓰지 않는다. 각자 목적에 맞게 쓰도록 하자***

---

# 참고

### 1. 매직 메서드

- 인스턴스 메서드
- 직접 활용은 안 함
- 특정 상황에 자동으로 호출되는 메서드
- Double underscore 가 있는 메서드는 특수한 동작을 위해 만들어진 것
- 스페셜 메서드 혹은 매직 메서드라고 불림
- ‘__init__’ 과 ‘__str__’를 주로 씀

### 2. 데코레이터

다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

```python
"""
데코레이터 정의
"""
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper

"""
데코레이터 정의
"""
@my_decorator
def my_function():
    print('원본 함수 실행')

my_function()

"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
```

my_function 을 수정하지 않고 **무언가 기능 추가하기 위해서** 사용

*→ 직접 구현할 필욘 없고 역할만 알아두자*

---

# 실습

```python
'''
생성자 메서드 구조로 class singer 선언후
1. 인스턴스 속성 출력
2. 인스턴스 메서드 호출
3. 인스턴스 변수 이름 : member 로 만들기
4. 인스턴스 속성 : 가수 / 1993 년 5 월 16 일 / 대한민국
5. 메서드 : 랩, 댄스, 소몰이 만들기
'''

class Singer:
    def __init__(self):
        self.job = '가수'   # self.어쩌구 : 멤버 변수
        self.birth = '1993년 5월 16일'
        self.country = '대한민국'

    def rap(self):  # self 매개변수를 통해 해당 객체에 접근
        print('랩 하기')
    
    def dance(self):
        print('댄스 추기')

    def sing(self):
        print('소몰이 부르기')

# 클래스에 대한 인스턴스 생성
member = Singer()

# 인스턴스 속성 출력
print(f'직업 : {member.job}')
print(f'생년월일 : {member.birth}')
print(f'국적 : {member.country}')

# 인스턴스 메서드 호출
member.rap()
member.dance()
member.sing()
```

```python
'''
my_count 라는 메서드 직접 만들기
클래스 명은 MyStr

조건1. 생성자 메서드 구조
조건2. 클래스 변수와 멤버 변수 생성
조건3. 기능은 count()메서드와 같은 기능
'''

class MyStr:
    # 클래스 변수 count 초기화
    # count = 0
    def __init__(self, string):
        # 멤버 변수 string 을 생성자에서 초기화
        self.string = string
        # self.count = None : 멤버변수 카운트 초기화
      
    def count_method(self, char):
        self.count = self.string.count(char)
        return self.count
# self.count와 self.string.count 의 차이? 멤버변수 self.string 초기화 이유는?
# 클래스 변수 count 는 반드시 있어야 하는 것은 아님 -> 멤버변수로 넣어도됨
# 클래스 변수의 역할 : 클래스 변수로 데이터를 추적하거나 데이터 공유
# 멤버 변수의 역할 : 멤버 변수로 데이터를 추적하거나 데이터 개별화

my_str = input()
my_instance = MyStr(my_str)
result = my_instance.count_method('i')
print(result)
```
