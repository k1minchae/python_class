<aside>
💡 데이터 구조 中 비 시퀀스 자료 → set / dict

</aside>

# 비시퀀스 데이터 구조

- 메서드 호출 방법 : ***데이터 타입 객체.메서드()***
- 비시퀀스 : 순서가 없다
    
    ```python
    my_set = {'a', 'b', 'c', 1, 2, 3}
    print(my_set)   # {1, 2, 3, 'a', 'b', 'c'} 순서가 없다.
    ```
    

## 1. set

- 고유한 항목들의 정렬되지 않은 컬렉션
- 빈 세트 만드는 법 : set()
    
    ( { }로 만들면 딕셔너리가 만들어진다. )
    
- **세트 메서드는 원본 세트를 변경한다.**
    
    → 변경하지 않으려면? 복사본 만들어서 작업
    

1. ***s.add(x)*** : 항목 x 추가 (이미 있다면 변화 없음)
    - list의 append와 비슷함 (단, append는 마지막에 추가)
    
    ```python
    my_set.add(4)
    print(my_set)   # {'a', 1, 2, 3, 'c', 4, 'b'}
    
    my_set.add(4)
    print(my_set)   # {'a', 1, 2, 3, 'c', 4, 'b'}
    # 이미 있다면 변화 X (중복이 안 된다)
    ```
    
2. ***s.clear()*** : 모든 항목 제거
    
    ```python
    print(my_set)   # {'a', 1, 2, 3, 'c', 4, 'b'}
    
    my_set.clear()
    print(my_set)   # set() <- 빈 세트 표기법
    ```
    
3. ***s.remove(x)*** : 항목 x 제거 (없을 경우 error)
    
    ```python
    print(my_set)   # {'a', 1, 2, 3, 'c', 4, 'b'}
    
    my_set.remove('a')
    print(my_set)   # {1, 2, 3, 4, 'b', 'c'}
    my_set.remove('z')
    print(my_set)   # KeyError: 'z'
    ```
    
4. ***s.pop()*** : **임의로** 항목 **반환**, 제거 **(≠ 랜덤하게)**
    
    ```python
    element = my_set.pop()  # my_set = {1, 2, 3, 4, 'c', 'b'}
    print(element)  # 1 이 가장 많이 나옴
    
    # 세트의 모습에 따라 어떤 값이 빠질 지 바뀜
    # 우리가 생각하는 랜덤의 확률과는 다르다.
    # 알파벳만으로만 구성된 set 는 우리가 생각하는 랜덤임
    ```
    
    → List 에서는 마지막 항목 반환, 제거
    
5. ***s.discard(x)*** : 항목 x 제거 **(없어도 error 안 생김 ≠ remove)**
    
    ```python
    my_set = {1, 2, 3}
    my_set.discard(1)
    print(my_set)    # {2, 3}
    
    my_set.discard('z') # 없는 값을 discard 하면 ?
    print(my_set)   # {2, 3} (오류 X)
    ```
    
6. ***s.update(iterable)*** : 세트에 다른 iterable 요소 추가
    
    → List 의 extend와 유사함
    
    → iterable 요소를 풀어서 넣어줌
    
    ```python
    my_set = {'a', 'b', 'c', 1, 2, 3}
    my_set.update([1, 4, 5])
    print(my_set)   # {'c', 1, 2, 3, 'a', 4, 5, 'b'}
    
    # 1은 중복이라 들어가지 않음.
    ```
    

### 세트의 집합 메서드



```python
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
```

---

## ★ 2. dict

- 고유한 항목들의 정렬되지 않은 컬렉션 **(중복X)**
- key : value 형태의 자료형
- 다른 프로그래밍 언어도 다 가지고 있는 형태의 데이터 타입
- **update() / clear() 빼고 다 반환**

### 딕셔너리 메서드



1. ***.get(x)*** : 키에 연결된 값 반환
    
    ```python
    print(person.get('name'))   # Alice
    print(person['name'])   # Alice
    
    print(person.get('country'))    # None
    # 키가 없을 경우 (Error X) None 반환
    # person['country'] 로 찾으면 에러가 난다.
    
    print(person.get('country', '기본값 : 키가 없습니다.')) 
    # 출력 : 기본값 : 키가 없습니다.
    # 키가 없을 경우 키에 연결된 기본값 반환
    ```
    
2. ***.keys()*** : 딕셔너리의 키를 모은 객체 반환
    
    ```python
    print(person.keys())    
    # dict_keys(['name', 'age']) -> dict_keys type
    # 대괄호로 감싸져있음 
    (순서가 나열되어 있다. -> 반복 가능한 객체)
    
    for k in person.keys():
        print(k)    
        # name
        # age
    ```
    
3. ***.values()*** : 딕셔너리 값을 모은 객체 반환
    
    ```python
    print(person.values())
    # dict_values(['Alice', 25])
    
    for i in person.values():
        print(i)    
        # Alice
        # 25
    ```
    
4. ***.items()*** : 딕셔너리 키/값 쌍을 (튜플로) 모은 객체 반환
    
    ```python
    print(person.items())
    # dict_items([('name', 'Alice'), ('age', 25)])
    
    for key, value in person.items():
        print(key, value)
        # name Alice
        # age 25 (언패킹)
    ```
    
5. ***.pop(key[,default])*** : 키를 제거하고 연결됐던 값 반환
    
    → 없으면 에러나 default 반환
    
    ```python
    print(person.pop('name'))   # Alice -> 반환
    print(person)   # {'age': 25} -> 'name' 키/값 제거됨
    print(person.pop('country'))    # KeyError
    print(person.pop('country', 'Default')) # Default
    ```
    
6. ***★ .setdefault(key[,default])*** : 키와 연결된 값 반환
    
    **→ 키가 없다면 연결한 키를 추가하고 default반환**
    
    → IF 문을 줄일 수 있다.
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    print(person.setdefault('country', 'Korea'))    # Korea
    print(person)   
    # {'name': 'Alice', 'age': 25, 'country': 'Korea'}
    ```
    
7. ***.update([other])*** : 값 추가할 때 유용하게 사용
    
    → 기존 키는 덮어쓰고 other가 제공하는 key/value 쌍으로 **갱신**
    
    ```python
    person = {
            'name': 'Alice', 
              'age': 25
    }
    
    other_person = {
        'name': 'Jane',
        'gender': 'Female'
    }
    
    # other_person 에 있는 데이터를 person에 넣고싶다.
    person.update(other_person)
    print(person)   
    # 출력 : {'name': 'Jane', 'age': 25, 'gender': 'Female'}
    # 단, 중복된 key는 원본 값이 사라짐
    
    person.update(age= 50, country='korea')  # 키워드인자 사용O
    # 출력 : {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'korea'}
    print(person)
    ```
    

**★ dict 메서드인 get, pop, setdefault 의 공통점과 차이점 ★**

- 공통점 : value 를 반환한다.
- 차이점 :
    - get → search 기능 (원본 변경X)
    - pop → remove 기능 (원본 변경O)
    - setdefault → add 기능 (원본 변경O)

```python
# 4. division 제거 (2가지 방법)
my_dict.pop('division')
del my_dict['division']
print(my_dict)
```

---

## 참고

→ 그래도 중요함

### 해시 테이블

- **해시 함수** 사용 **≠ hash()**
- **변환(return)** 값을 **index**로 삼아 key와 value 저장하는 **자료구조**
- 데이터를 효율적으로 저장 / **검색**

```python
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
```

- 키를 해시 함수를 통해 해시값으로 변환하고, 그 값을 기반으로
    
    bucket 안에 **고유한** 위치에 대응 → **무결성**
    
    이 해시값을 인덱스로 사용하여 데이터를 저장하거나 검색
    
    **→ 순서가 상관 없다.** (set, dict와 유사)
    
- 가변데이터는 안 됨
- 데이터 검색이 빨리 이루어짐

### 해시

- 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
    

    
- 이렇게 생성된 고유한 값은 주로 해당 데이터를 **식별하는데 사용**될 수 있음 (일종의 ‘지문’의 역할 → 데이터를 고유하게 식별)
- 파이썬에선 이 해시함수를 사용해서 데이터를 해시값으로 변환
    
    **→ 이 해시 값은 정수로 표현됨**
    

### 해시 함수

- 임의의 길이의 데이터를 입력받아
    
    고정된 길이의 데이터(해시값)을 출력하는 함수
    

**★ 해시테이블의 해시함수 ≠ hash()**

- 주로 해시테이블 자료구조에 사용.
- 매우 빠른 데이터 검색, 저장을 위한 컴퓨터 소프트웨어에서 주로 사용
- hash() : 객체의 해시 코드를 반환하는 파이썬 내장함수

### set와 dict의 키와 해시테이블 관계

- 세트의 요소 /dict의 key는 해시테이블 이용 → 중복X 고유의 값 저장
- 순서x → 해시함수를 거쳐야만 고정된 위치를 알 수 있다.
- 해시함수 → 해시값으로 변환 후 해시테이블에 저장
    
    **(키 → 함수 → 해시코드로 변환 → 해시테이블에 저장)**
    
- 딕셔너리 키 : 고유해야 함
- 딕셔너리는 매우 빠른 검색속도 제공 / 중복 허용 X

### set의 pop메서드 예시 (정수)

- **정수 값 자체가 곧 해시 값 (항상 같은 색인 값)**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/817e8200-27cc-4ffe-8d29-f38fd233977c/aaa90789-e0bc-4756-81be-cbd3e3b41c12/Untitled.png)
    
    → pop 메서드는 요소를 임의로 반환한다면서 왜 이렇게 나오는지 ? 
    
    → 정수는 이미 해시값을 갖고 있다. (굳이 랜덤의 수를 줄 필요X)
    
    **(해시테이블에 나열된 순서)**
    
    **(오름차순X,  세트에 나열된 순서X)**
    
    → 정수는 값이 변하지도 않고 type 도 똑같고 굳이 문제 발생 X
    
    **→ 단 , 문자는 매번 임의로 색인 값을 부여받는다. (≠ 랜덤)**
    

### 파이썬 해시 함수 : hash() → 해시코드 반환 내장 함수

```python
print(hash(1))  # 1
print(hash(1))  # 1
print(hash('a'))    # 실행시마다 다름
print(hash('b'))    # 실행시마다 다름
```

- 동작 방식은 객체의 타입에 따라 달라짐
- 정수와 문자열은 서로 다른 타입. (계산 방식도 다름)
- 세트와 딕셔너리는 index가 없다고했는데?
    
    **해시테이블 인덱스 ≠ 시퀀스 자료형 인덱스(요소의 위치)**
    
    → 해시함수에 넣으면 해시테이블 bucket이라는 곳에 들어감
    
    ***(해시테이블의 인덱스 : 해시함수에 의해서 계산되는 값 ≠ 요소 위치)***
    

1. **정수**
    - 항상 같은 해시값 (고정)
    - 단, 오름차순 X 순서 X
2. **문자열**
    - 문자는 가변적인 길이를 가짐
    - 각 유니코드의 코드 포인트를 기반으로 해시값 계산
    - 문자열의 해시 값은 실행시마다 다르게 계산됨
    - **랜덤 (매번 테이블에서 랜덤 순서로 뽑는다) → 아님!!**
    - **임의값 (테이블에서 배치된 순서대로 반환 * 단 배치 매번 바뀜) → 맞음!!**

### Hashable

- hash() 함수의 인자로 전달해서 결과를 반환받을 수 있는 객체
- 대부분의 불변형 데이터 타입은 hashable
- 단, 튜플은 불변형이지만 안에 가변데이터를 넣을 수 있음 → 그럴 땐 **해시 불가능해짐**
    
    ***→ hash((1, 2, [3, 4])) → 안 됨***
    
- 가변 객체는 값이 변경될수 있기 때문에 동일한 객체에 대한 해시 값이 변경될 수 있다. → **해시 테이블의 무결성 유지 불가**
- **따라서, 해시 테이블의 키는 불변해야 함**
    
    (객체 생성 이후 값 변경X)
    
- 불변 객체는 해시 값 변화 X → 동일한 값은 일관된 해시값 유지O
- **단, 해시 가능하다 ≠ 불변하다**

### hashable 객체가 필요한 이유

- 해시테이블 기반 자료구조 사용을 위해
    - set와 dict의 key
    - 중복값 방지
    - 빠른 검색, 조회
- 불변성을 통한 일관된 해시 값
- 안정성과 예측가능성 유지

---

# 실습

```python
my_dict = {
    'plus': ['더하기', '장점'],
    'minus': ['빼기', '적자'],
    'multiply': ['곱하기', '다양하게'],
    'division': ['나누기', '분열']
}

# 1. '빼기' 반환
print(my_dict.get('minus')[0])
print(my_dict['minus'][0])
print(my_dict.pop('minus')[0])
print(my_dict.setdefault('minus')[0]) 

# 2. key 값 순차적으로 출력
for i in my_dict.keys():
    print(i, end=' ')
print()

# 3. 'square' : ['제곱', '사각형'] 추가 (3가지 방법)
my_dict.setdefault('square', ['제곱', '사각형'])
my_dict['square'] = ['제곱', '사각형']

my_dict.update(square = ['제곱', '사각형'])

dict_2 = {'square': ['제곱', '사각형']}
my_dict.update(dict_2)

# 4. division 제거 (2가지 방법)
my_dict.pop('division')
# my_dict.
print(my_dict)
```