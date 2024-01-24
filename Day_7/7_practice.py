# 클래스 정의
class Person:
    # 클래스 변수 (속성) -> 클래스 내부에 선언된 변수
    blood_color = 'red' # 클래스의 모든 인스턴스들이 '공유'하는 변수


    # 생성자 함수
    def __init__(self, name):  # self : 인스턴스 자기 자신
        self.name = name    # 인스턴스 변수 : 인스턴스마다 독립적인 값 (생성될때마다 초기화 됨)

    # - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
    # - __init__ 이라는 이름의 메서드로 정의하며, 객체 초기화 담당
    # - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값 설정



    # 인스턴스 메서드
    def singing(self):  # 인스턴스가 쓸 수 있는 메서드
        return f'{self.name}가 노래합니다.'

    # - 각각의 인스턴스에서 호출 가능한 메서드
    # - 각각의 인스턴스 변수에 접근하고 수정가능


# 인스턴스 생성 -> __init__ 호출
singer1 = Person('IU')  
singer2 = Person('bts')

# 메서드를 호출
print(singer1.singing())    # IU가 노래합니다.
print(singer2.singing())    # bts가 노래합니다.

# 속성 접근
print(singer1.blood_color)  # red
print(singer2.blood_color)  # red


##########구분선############
'''
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
'''
##########구분선 ##############
'''
class MyClass:

    def instance_method(self, arg1):    # self 쓰고 그뒤에 추가인자 쓰면됨
        pass

# self 동작 원리

# upper 메서드를 통해 대문자로 변경
'hello'.upper()

# 파이썬 내부 동작
str.upper('hello')
# str 클래스가 upper 호출 -> 그 인자로 인스턴스 들어감
'''



'''
실습
생성자 메서드 구조로 class singer 선언후
1. 인스턴스 속성 출력
2. 인스턴스 메서드 호출
3. 인스턴스 변수 이름 : member 로 만들기
4. 인스턴스 속성 : 가수 / 1993 년 5 월 16 일 / 대한민국
5. 메서드 : 랩, 댄스, 소몰이 만들기


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


# 실습 2


# my_count 라는 메서드 직접 만들기
# 클래스 명은 MyStr

# 조건1. 생성자 메서드 구조
# 조건2. 클래스 변수와 멤버 변수 생성
# 조건3. 기능은 count()메서드와 같은 기능



class MyStr:


    def __init__(self, string):
        # 멤버 변수 string 을 생성자에서 초기화
        self.string = string

      
    def count_method(self, char):
        count = 0   # count 지역변수
        for letter in self.string:
            if letter == char:
                count += 1
        return count
# self.count와 self.string.count 의 차이? 멤버변수 self.string 초기화 이유는?
# 클래스 변수 count 는 반드시 있어야 하는 것은 아님 -> 멤버변수로 넣어도됨
# 클래스 변수의 역할 : 클래스 변수로 데이터를 추적하거나 데이터 공유
# 멤버 변수의 역할 : 멤버 변수로 데이터를 추적하거나 데이터 개별화

my_str = input()
my_instance = MyStr(my_str)
result = my_instance.count_method('i')
print(result)
'''


# 실습 3: 클래스 메서드는 클래스 레벨에서 동작하며 , 
#        cls매개변수를 통해 클래스 자체에 접근한다.
# 실습 1에서 했던거 클래스 메서드로 바꾸기

# class Singer:
#     # 클래스 변수
#     job = '가수'   
#     birth = '1993년 5월 16일'
#     country = '대한민국'

#     @classmethod
#     def rap(cls):  
#         print('랩 하기')
    
#     @classmethod
#     def dance(cls):
#         print('댄스 추기')
    
#     @classmethod
#     def sing(cls):
#         print('소몰이 부르기')

# # 클래스에 대한 인스턴스 생성
# member = Singer()

# # 인스턴스 속성 출력
# print(f'직업 : {member.job}')
# print(f'생년월일 : {member.birth}')
# print(f'국적 : {member.country}')

# # 클래스 메서드 호출
# Singer.rap()
# Singer.dance()
# Singer.sing()

# 실습 4 : 스태틱 메서드 : 클래스나 인스턴스와는 무관하게 독립적으로 동작하는 메서드
# 클래스 내부에서 선언되지만 클래스 변수에는 접근하지 않는다.


# class Singer:
#     # 클래스 변수
#     job = '가수'   
#     birth = '1993년 5월 16일'
#     country = '대한민국'

#     @staticmethod
#     def rap():  
#         print('랩 하기')
    
#     @staticmethod
#     def dance():
#         print('댄스 추기')
    
#     @staticmethod
#     def sing():
#         print('소몰이 부르기')

# # 클래스에 대한 인스턴스 생성
# member = Singer()

# # 인스턴스 속성 출력
# print(f'직업 : {member.job}')
# print(f'생년월일 : {member.birth}')
# print(f'국적 : {member.country}')

# # 스태틱 메서드 호출
# Singer.rap()
# Singer.dance()
# Singer.sing()

