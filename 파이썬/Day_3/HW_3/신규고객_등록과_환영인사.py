number_of_people = 0  

def increase_user():
    global number_of_people  
    number_of_people += 1    

    print(f'현재 가입 된 유저 수 : {(number_of_people) - 1}')

increase_user() 

def create_user(name, age, adress):
    print(f'{name}님 환영합니다!')
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = adress
    print(user_info)

create_user('홍길동', 30, '서울')
increase_user()