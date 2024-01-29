# 상속

기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스 생성

### 필요한 이유

1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성, 메서드 재사용 가능
    - 새로운 클래스 작성 시 기존 클래스 기능 활용 가능
    - 중복된 코드 줄일 수 있음
2. 계층구조
    - 상속을 통해 클래스들 간의 계층구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계 표현
    - 더 구체적인 클래스 만들기 가능
3. 유지 보수의 용이성
    - 기존 클래스의 수정이 필요한 경우 해당 클래스만 수정하면 됨
    - 코드의 일관성 유지 + 수정 범위 최소화

### 상속 없이 구현할 경우

- 학생/교수 정보를 나타내기 어려움
    
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
    
    class Professor():
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
    
    class Student():
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa
    
    s1 = Person('김학생', 23)
    s1. talk()
    
    p1 = Person('박교수', 59)
    p1. talk()
    ```
    

- 상속시켜보기
    
    ```python
    class Professor(Person):  # Person 으로부터 상속받음 
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
    
    class Student(Person):
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa
    
    p1 = Professor('김교수', 59, '컴퓨터공학과')
    s1 = Student('김학생', 23, 3.8)
    
    print(p1.department)    
    print(s1.gpa)   
    
    p1.talk()   # 부모 클래스의 메서드 사용 가능
    s1.talk()
    ```
    
- 메서드 중복 정의
    
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
    
    class Professor(Person):  # Person 으로부터 상속받음 
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
        
        def talk(self):    # 메서드 중복
            print('잘 부탁드립니다.')
    
    p1 = Professor('김교수', 59, '컴퓨터공학과')
    p1.talk()    # '잘 부탁드립니다.'
    ```
    
    - 부모 클래스에 있어도 자식 클래스에 같은 메서드 정의 가능
    - 단, 본인 메서드에 있는걸 가장 우선으로 사용한다.
    

### super()

부모 클래스 객체를 반환하는 내장 함수

- 부모 클래스의 생성자 함수 가져오기
    
    ```python
    class Student(Person):
            # 상속을 하더라도 인자는 다 적어줘야 함
        def __init__(self, name, age, number, email, student_id):
    
            # 부모 클래스에서 __init__을 호출 (person.init)
            super().__init__(name, age, number, email)
            Person.__init__(name, age, number, email) # 과 같음
            # 단, 이렇게 안씀 (Person 이름이 바뀌면 다 바꿔야해서)
    
            self.student_id = student_id # 중복 아닌것 써주기
    ```
    

### 다중 상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받음
- 상속받은 모든 클래스의 요소 활용 가능
- 중복된 속성, 메서드 있는 경우 **상속 순서에 의해 결정됨**
    
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
    
        def greeting(self):
            return f'안녕, {self.name}'
    
    class Mom(Person):
        gene = 'XX'
    
        def swim(self):
            return '엄마가 수영'
    
    class Dad(Person):
        gene = 'XY'
    
        def walk(self):
            return '아빠가 걷기'
    
    # 다중 상속 받는 클래스
    class FirstChild(Dad, Mom): # 그냥 나열하면 됨
        def swim(self):
            return '첫째가 수영'
        
        def cry(self):
            return '첫째가 응애'
        
        
    # 생성자 함수 없으면 상속받은 위로 올라가서 찾아야 함
    baby1 = FirstChild('김싸피')
    
    # 본인의 인스턴스 메서드 실행
    print(baby1.cry())  
    print(baby1.swim())
    
    # 아빠의 메서드 실행
    print(baby1.walk()) # 아빠가 걷기
    
    # 성별은 부모 클래스의 중복된 속성
    print(baby1.gene)   # XY
    # 다중상속 할 때 아빠 클래스를 먼저 적었기 때문에 중복시 아빠것으로 결정된다.
    ```
    

- 다이아몬드 문제
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/817e8200-27cc-4ffe-8d29-f38fd233977c/73db28a3-9eb3-4c43-a4bf-016f6a0f234a/Untitled.png)
    

- B와 C 모두에서 D가 상속됨
- B C가 모두 A 에서 상속됨
- D는 B의 메서드 중 어느 버전을 상속하는가 ?
- 아니면 C의 메서드 버전을 상속하는가 ?

**해결책 (Method Resolution Order : 메서드 결정 순서)**

- 부모 클래스로부터 상속된 속성들의 검색을 **깊이 우선으로,**
- **왼쪽에서 오른쪽**으로 검색하며 → **같은 클래스를 두번 검색하지 않음**
- 그래서 속성이 D에서 발견되지 않으면 B에서 찾고, 거기에서도 없으면 C에서 찾는 방식

### super()

부모 클래스 객체를 반환하는 내장함수

→ 다중 상속시 MRO를 기반으로 호출될 메서드를 자동으로 결정해줌

```python
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # 여기서의 super는 부모A
        self.value_C = 'Child'

    def show_value(self):
        super().show_value()    # super -> 부모A
        print(f'Value from Child : {self.value_C}')

child = Child()
child.show_value() 
print(child.value_a)    # ParentA
print(child.value_C)    # Child
# print(child.value_b)    # 'Child' object has no attribute 'value_b'
# child는 b의 생성자함수를 쓰지 않았기 때문에. (A한테 있어서)
```

### super()의 사용 사례

1. 단일 상속 구조
    - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로 코드를 유지 관리하기 쉽게 만들 수 있다
    - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 적어진다
2. 단일 상속 구조
    - MRO를 따른 메서드 호출
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제 방지

### 함수의 콜스택

```python
class A:
    def __init__(self):
        print('A Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')

class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')
# 다이아몬드 상속

obj = D()
'''
A Constructor
C Constructor
B Constructor
D Constructor
'''
# 콜스택 : (제일 마지막에 있던게 먼저 호출되는)
# 쌓여있다가 A 가 호출되고 빠지고 순차적으로 호출됨

print(D.mro())  # super 가 호출하는 순서 알려줌
'''
[<class '__main__.D'>, 
<class '__main__.B'>, 
<class '__main__.C'>, 
<class '__main__.A'>, 
<class 'object'> -> 클래스를 만들어내는 클래스 - 무시해도됨]
'''
```

- mro() 메서드
    - 해당 인스턴스의 클래스가 어떤 부모클래스를 가지는지 확인하는 메서드
    - 기존 인스턴스 → 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 → 자식클래스 → 부모클래스로 확장
    - 부모 클래스들이 여러번 액세스 되지 않도록, **순서 보장**
    - 부모를 오직 한 번만 호출하고 우선순위에 영향 X
    - **단조적인 구조를 형성한다**

---

# 에러와 예외

### 버그

- 소프트웨어에서 발생하는 오류, 결함
- 프로그램의 예상된 동작과 실제 동작 사이의 불일치
- 기원 : Mark 2 컴퓨터 회로에 나방이 들어가 합선 → 비정상 동작
- 디버깅 : 버그를 찾아내고 수정하는 과정

### 디버깅 방법

1. print함수 활용
2. 개발 환경(text editor, IDE) 에서 제공하는 기능 활용
3. Python tutor 활용 (단순 파이썬 코드인 경우)
4. 뇌 컴파일, 눈 디버깅

### 에러

- 종류: 문법 에러 & 예외
1. 문법 에러
    - 프로그램의 구문이 올바르지 않은 경우
    - 할당을 잘못 했거나 괄호 빼먹거나
2. 예외
    - 프로그램 실행 중에 감지되는 에러

### 내장 예외

예외 상황을 나타내는 예외 클래스들

→ 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용

- 예시
    - ZeroDivisionError : 0으로 나누려 할 때
    - name_error : 지역, 전역이름을 찾을 수 없을 때
    - Type_error : 문자열 + 정수
    - 인자 누락 (Ex. Sum() ) // 인자 초과 ( sum(1, 2, 3) ) // 인자 타입 불일치
    - ValueError : 부적절한 값을 가진 인자를 받은 경우
        
        → int(’1.5’) // range(3).index(6)
        
    - indexError : 시퀀스 인덱스가 범위를 벗어날 때 (out of range)
    - keyError : 딕셔너리에 해당 키가 존재하지 않을 때
    - ModuleNotFoundError : 모듈을 찾을 수 없을 때
    - ImportError : 임포트하려는 이름을 찾을 수 없을 때
    - KeyboardInterrupt : 사용자가 Ctrl + C 또는 Del 누를때 (강종)
    - IndentationError : 잘못된 들여쓰기 등 문법오류

### try와 except

- try 문과 except 절을 사용해서 예외 처리
- try 블록에서 예외가 발생하면 즉시 대응된 except 블록으로 이동
    
    ```python
    try:
        # 예외가 발생할 수 있는 코드
        num = int(input('숫자 입력 : '))
        print(100 / num)
    
    except ValueError: # 특정 예외 입력
        # 예외 처리 코드
        print('숫자가 아닙니다.')
    
    except ZeroDivisionError:
    	  print('0으로 나눌 수 없습니다.')
    
    except: 
        # 예외 옆에 아무것도 안 쓰면 모든 예외를 받는다.
        print('알수없는에러')
    
    -----------------------------------------------------
    
    try: 
        result = 10/0
    
    except ZeroDivisionError, ValueError:
        print('잘못된 값을 입력했습니다.')
    ```
    
- 내장 예외 클래스는 상속 계층구조를 가진다.
- **하위클래스를 먼저 확인할 수 있도록 작성해야 함**

### as 키워드

- as 키워드를 활용하여 에러메세지를 except 블록에서 활용 가능



---

### EAFP

- 허락보다 용서가 쉽다
- 예외처리를 중심으로 코드를 작성하는 접근 방식
    
    → 일단 코드실행하고 나중에 처리 (try - except 방식)
    

### LBYL

- 돌다리도 두들겨보고 건너라
- 값 검사를 중심으로 코드를 작성하는 접근 방식 (if - else)

### 비교

```python
# try-except
try: 
    result = my_dict['a']    
    print(result)
except KeyError:
    print('키가 없습니다.')

# if-else
if 'a' not in my_dict:
    result = my_dict['a']    
    print(result)
else:
    print('키가 없습니다.')
```

| EAFP | LBYL |
| --- | --- |
| “일단 실행하고 예외를 처리” | “실행하기 전에 조건 검사” |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전에 조건문 등을 사용하여예외 상황을 미리 검사하고 예외상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 뒤 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음 |
| 예외 상황을 예측하기 어려운 경우에 유용함 | 예외 상황을 미리 방지하고 싶을 때 유용함 |

---

# 실습

### 다중상속

```python
# 다중상속 실습

class Car:
    def __init__(self, model):
        self.model = model

class Hyundai(Car):
    color = "white"

    def speed(self):
        return "30km/h"
    
class Kia(Car):
    color = "black"

    def engine(self):
        return "1.6 turbo"

class CarDrive(Hyundai, Kia):
    def speed(self):
        return "50km/h"
    
    def power(self):
        return '1,999cc'

car = CarDrive('Sonata')
print(car.speed())  # 50km/h
print(car.color)    # White

MRO 에따라 클래스 변수는 값을 찾으면 멈춤
메서드 오버라이드 : 메서드는 MRO 에 따라 가장 마지막에 정의된 메서드 호출

```