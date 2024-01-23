# 아래 함수를 수정하시오.
'''
my_set순회해서 얻은 값을 key로 하는 my_dict의 값 출력
    a. 순회중에 얻은 키가 my_dict에 없다면 None출력
    b. get 메서드 활용

var 변수에 dict 의 키로 사용가능한 자료형 할당
my_dict에 var변수를 key로 하는 value '변수로도 키 설정 가능' 문자열 할당
변경된 my_dict 출력

'''

my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for i in my_set:
    print(my_dict.get(i))

var = (1, 2, 3, 'A')
my_dict.setdefault(var, '변수로도 키 설정 가능')
print(my_dict)