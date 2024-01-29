number_of_people = 0


def increase_user():
    global number_of_people  
    number_of_people += 1    


all_user = []   # for 안에 넣으면 초기화돼서 밖으로 빼야함
def create_user(name, age, adress):
    print(f'{name}님 환영합니다!')
    for i in range(0, 5):
        user_info = {}
        user_info['name'] = name[i]
        user_info['age'] = age[i]
        user_info['address'] = adress[i]
        print(f'{name[i]}님 환영합니다!')
        all_user.append(user_info)
    print(all_user)



name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
create_user(name, age, address)
