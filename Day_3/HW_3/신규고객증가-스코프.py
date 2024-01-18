'''주어진 코드
number_of_people = 0 -> 글로벌


def increase_user():
    number_of_people += 1


increase_user()
print(number_of_people)

# 로컬변수에 접근할 수 없다고 나옴
'''

# 코드를 수정하시오.

number_of_people = 0  # 전역 변수로 초기화

def increase_user():
    global number_of_people  # 전역 변수임을 명시
    number_of_people += 1    # 전역 변수 값 증가

    print(number_of_people)

increase_user()
increase_user()

'''
함수 내에서 number_of_people를 로컬 변수로 선언하면 
매번 함수가 호출될 때마다 새로운 로컬 변수가 생성되어 값이 유지되지 않습니다. 
따라서 함수가 호출될 때마다 number_of_people가 1로 초기화되고 증가합니다.

함수 내에서 변수를 로컬로 선언하지 않고, 
전역 변수로 사용하려면 global 키워드를 사용하여 전역 변수임을 명시해야 합니다.
'''