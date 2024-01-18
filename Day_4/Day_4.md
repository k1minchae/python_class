# 1/18(목)

# 모듈

- 한 파일로 묶인 변수와 함수의 모음
- 특정한 기능을 하는 코드가 작성된 파이썬 파일 (.py)
- 1 모듈 = 1파일

### 모듈 예시

- 파이썬의 math 모듈
- 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈
    
    ```python
    import math     # import 를 통해 파일을 가져오는 것 필요
    
    print(math.pi)  # 파이썬 어딘가에 math.py 가 저장되어있음
    print(math.sqrt(4))    # (제곱근 구하는 함수)
    
    # 내장함수 help를 사용해 모듈에 무엇이 들었는지 확인 가능
    help(math)
    ```
    

## 모듈 사용하기

- . (dot) 은 “점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라” 라는 의미의 연산자
    
    → 모듈명.함수명(인자)
    
- import 하는 다른 방법
    - from 절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import 할지 명시
        
        ```python
        from math import pi, sqrt    # pi, sqrt 만 import 함 (비권장)
        
        print(pi)
        print(sqrt(4))
        
        print(math.pi)    # 에러
        print(math.sqrt)    # 에러
        ```
        
- 모듈 주의사항
    - ***만약 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생***
    - 마지막에 import 된 이름으로 대체된다.
        
        ```python
        from math import *    # * 이 전체를 의미함 (전체다 import -> 비권장)
        from math import pi, sqrt    
        from my_math import sqrt    # 문제 발생
        # -> math import 로 했으면 충돌X (math.sqrt // my_math.sqrt)
        ```
        
- 직접 정의한 모듈 사용하기 (실습)
    - 모듈 my_math.py작성
    - 두수의 합을 구하는 add 작성
    - my_math 모듈 import 후 add함수 호출
    
    ```python
    # my_math.py
    def add(x, y):
        return x + y
    
    import my_math  # 동일한 경로에 있으면 바로 뜸
    print(my_math.add(1, 2))    # 3
    ```
    

---

# 파이썬 표준 라이브러리 (PSL)

- 파이썬 과 함께 제공되는 모듈과 패키지의 모음 (내장된 것)
- 공식문서에 들어가면 있다 ***(라이브러리 레퍼런스)***
- 변수, 함수가 많아졌을 때 유지보수를 용이하게 함
- 모듈로 비슷한 애들끼리 정리 하는 법 ?
- 모듈 < 패키지 < 라이브러리

### 패키지

- 관련된 모듈(.py)들을 하나의 디렉토리**(폴더)**에 모아 놓은 것
- 모듈들의 이름 공간을 분리하여 충돌을 방지 & 효율적 관리
- 모듈이 패키지 안에 있다면 ? → **from 활용**
    - my_package 안에 math 와 statistics 패키지가 있다. (총 3개)
    - 모듈이 2개가 있다. (math 안에 my_math // statistics 안에 tools)
    
    ```python
    from my_package.math import my_math  # my_package 안에 math 패키지 안에
    from my_package.statistics import tools  # my_package 안에 statistics 안에
    
    print(my_math.add(1, 2))
    print(tools.mod(1, 2))
    ```
    
1. PSL 내부 패키지 
    
    설치 없이 바로 import 하여 사용
    
2. ★ 외부 패키지 (자주 사용)
    - pip를 사용하여 **설치후 import 필요**
        
        *(pip란? 외부 패키지를 설치하도록 도와주는 패키지 관리 시스템)
        
    - https://pypi.org 에 등록된 pip 설치하면 됨
        
        → 터미널 창에 pip install name_of_package 입력
        

---

# 제어문

- 코드의 실행 흐름을 컨트롤 할 수 있게 하는 것
- 조건에 따라 코드 블록을 실행하거나 반복적으로 코드 실행

## 1. 조건문

- **if / elif / else**
- 주어진 조건식을 평가하여 **True 인 경우에만** 실행함
    
    ```python
    # 실행 순서 : 위에서 아래로 (True되면 멈춤)
    # 동시에 검사하는 것이 아니라 순차적으로 비교 -> ★ 순서 잘 짜기
    if 표현식:
        코드블록
    
    elif 표현식:
        코드블록
    
    else:    # 모두가 False 라면 실행되는 것
        코드블록
    ```
    
    ### 실습 문제
    
    연도를 입력받아 윤년 판별하기. 윤년이면 'leap year' 출력.
    
    - 단, elif는 사용하지 마시오.
    - 그렇지 않으면 'common year'출력.
    - 1. 연도가 4로 나누어 떨어지지만 100으로는 나누어떨어지지 않는다.
    - 2. 연도가 400으로 나누어 떨어진다.
    
    ```python
    year = int(input())
    
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print('leap year')
    else:
        print('common year')
    ```
    

## 2. 반복문

- 주어진 코드 블록을 여러번 반복해서 실행하는 구문
    1. 특정 작업을 반복적으로 수행 **(제한된 작업량에 따라) → For**
    2. 주어진 조건이 참인 동안 반복해서 실행 **→ While**

## 1) for 문

- 임의의 시퀀스*(str, tuple, list, range,…)* 항목들을 그 시퀀스에 들어있는 순서대로 반복
    
    ```python
    # for 변수 in 반복 가능한 객체(Iterable: 시퀀스, dict, set, ...):
    #     코드블록
    ```
    
- 문자열도 순회가 가능하다. (’Korea’ → 한글자씩 순회함)
- dict를 반복문에 넣으면 ?
    
    ```python
    my_dict = {
        'x': 10,
        'y': 20,
        'z': 30,
    }
    
    for key in my_dict:
        print(key) # dict 는 반복돌리면 key만 나옴.
        print(my_dict[key]) # key도 출력하려면
    ```
    
    - for 문을 쓸 때 변수 이름은 최대한 직관적으로 사용한다.
    - matrix 순회할 때 쓰는 변수는 웬만하면 i, j, k, ,,,y,,,x 순으로 사용
    
- index 값을 활용하여 문제풀이
    
    ```python
    numbers = [4, 5, 10, -8, 5]
    
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    
    print(numbers)  # [8, 10, 20, -16, 10]
    ```
    
- 중첩된 반복문
    
    ```python
    outers = ['A', 'B']
    inners = ['c', 'd']
    
    for outer in outers:
        for inner in inners:    # 안쪽 for 문 루프가 끝난 뒤 바깥쪽으로 넘어 감
            print(outer, inner)
    # 출력 : A, c // A, d // B, c // B, d
    ```
    
- 중첩 리스트 순회
    
    안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩반복을 사용해 각 안쪽 반복을 순회
    
    ```python
    elements = [['A', 'B'], ['c', 'd']]
    
    for elem in elements:
        for item in elem:  # print(elem) : ['A', 'B'] \n ['c', 'd']
            print(item)    # print(item) : A \n B \n C \n D
    ```
    
- 트리만들기
    
    ```
    ''' for 문 실습 : 트리만들기
    정수 n 을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램 작성
    '''
        # 내가 푼 것
    # n = int(input('n : '))
    
    # for i in range(1, 1 + n):
    #     print(i * '*')
    
    #     # 답
    n = int(input())
    for i in range(n):
        for j in range(i + 1):
            print('*', end= '')
        print()
    ```
    

## 2) while 문

- **반드시 종료조건이 필요하다.**
- 주어진 조건식이 True 인 동안 코드를 반복해서 실행
- 조건식이 False 가 되면 멈춘다.
    
    ```python
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
    ```
    
- 사용자 입력에 따른 반복
    
    ```python
    number = int(input('양의 정수를 입력해주세요 : '))
    
    while number <= 0:
        if number < 0:
            print('음수를 입력했습니다.')
        else:
            print('0은 양의 정수가 아닙니다.')
        number = int(input('양의 정수를 입력해주세요. : ')) # 음수 넣을때마다 재입력 받음
    print('잘했습니다!')    # 양수 넣을경우 종료 및 프린트.
    
    '''
    양의 정수를 입력해주세요 : -3
    음수를 입력했습니다.
    양의 정수를 입력해주세요. : 0
    0은 양의 정수가 아닙니다.
    양의 정수를 입력해주세요. : -2
    음수를 입력했습니다.
    양의 정수를 입력해주세요. : 3
    잘했습니다!
    '''
    ```
    
- 실습 : while 문 + continue 를 사용하여 1~10까지 정수중 홀수만 출력하기
    
    ```python
    i = 0   # 초기식
    while i < 10: # 조건식
        i += 1  # 증감식
        if i % 2 == 0:
            continue
        print(i, end = '')
        print()
    ```
    

## 적절한 반복문 활용하기

1. for
    1. 반복 횟수가 명확하게 정해져 있는 경우에 유용
    2. 예를 들어 리스트 , 튜플, 문자열 등 시퀀스 형식의 데이터 처리
2. while
    1. 반복 횟수가 불명확 하거나 조건에 따라 반복을 종료해야 할 때 유용
    2. ***사용자의 입력을 받아서*** 조건이 충족 될 때 까지 반복할 때

## 반복 제어

- **break(중단) / continue(다음 반복으로 건너 뜀 → 처음으로 돌아감)**
- for, while 은 매 반복마다 본문 내 모든 코드를 실행하지만
- 때때로 일부만 실행하는 것이 필요할 때가 있음.
- for 문에 break 와 continue 둘 다 쓰는 연습 해보자. (문제에 나옴)

- **while에서 break 사용**
    
    ```python
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
    break : 수행중인 반복문(for, while)을 강제로 종료하는 역할
    실습 2 : 'shall we close? (y/n)' 문구에 y를 입력하면 반복문을 종료하고
    'the end'를 출력하는 프로그램을 작성해보세요.
    '''
    
    while True: # 무한 반복
        answer = input('shall we close? (y/n) ')
        if answer == 'y':
            print('the end')
            break
    ```
    
- **for 문에서 break 사용**
    
    ```python
    numbers = [1, 3, 5, 6, 7, 9, 19, 11]
    found_even = False  # 못찾을 때를 대비한
    
    for num in numbers:
        if num % 2 == 0:
            print('첫 번째 짝수를 찾았습니다:', num)
            found_even = True
            break   # 첫번째 짝수를 찾은 뒤 반복 종료하기.
    if not found_even:  
        print('짝수를 찾지 못했습니다')
    ```
    

- **contine 예시**
    
    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for num in numbers:
        if num % 2 == 0:
            continue    # 짝수일 경우 print 로 넘어가지 않고 다음 반복으로 건너뜀
        print(num)
    ```
    

- ***주의사항***
    
    단, break 와 continue 를 남용하는 것은 코드의 가독성을 저해할 수 있다.
    
    특정한 종료조건을 만들어 break를 대신하거나
    
    if 문을 사용해 continue를 대신할 수 있음.
    

---

# List Comprehension ★★

간결하고 효율적인 리스트 생성방법 (map대신)

- 형태
    
    ```python
    # 형태
    [Expression for 변수 in iterable]
    
    List(expression for 변수 in iterable)
    ```
    
- **활용 ★ (2차원 리스트 만들 때) ★**
    
    ```python
    rows = int(input()) # 행
    cols = int(input()) # 열
    
    # Comprehension 을 안 쓴 것.
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    
    # Q) 2차원 리스트 컴프리헨션을 사용하여 0으로 초기화된 2차원 리스트 생성
    
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    print(matrix)
    # 열의 개수만큼 0 이 append 가 되고 행의 개수만큼 append됨
    # comprehension을 쓰면 리스트를 초기화 할 필요가 없다.
    # if 문하고 같이 쓰는 것도 연습해보자.
    ```
    
- **주의 사항**
    
    너무 남용할 경우 가독성이 떨어진다.
    
    for 문과 if 문으로 만드는 것을 먼저 연습하고, list comprehension 으로 바꾸는 연습
    
    **알고리즘 풀 때는 자주 사용 ★**
    

---

### Pass

- 아무런 동작도 수행하지 않고 넘어가는 역할
- 문법적으로 문장이 필요하지만 프로그램 실행에는 영향X
- Django  할 때 사용함
- ***활용 방법***
    - 미완성 부분에 일단 pass 넣어놓고 나중에 추가
    - **code를 컴파일 하는동안 오류가 발생하지 않도록!!**
    - 조건문에서 아무런 동작도 수행하지 않아야 할 때
    - 무한루프에서 조건 충족이 안 될 때 pass를 통해 루프를 계속 실행하는 법

### Enumerate

iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

**for 인덱스, 요소** **in** **enumerate(iterable)**

인덱스 값을 요소와 함께 뽑아낼 수 있다!

→ 이런 것도 있다 ,,, 과목평가에는 나오기 좋음

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')
'''
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
'''
```

### JSON viewer

https://jsonviewer.stack.hu/

```python
Jason Viewer
import requests
url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()
print(response)
```

- 관통 프로젝트에서 활용한다.