number_of_people = 0


def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


many_user = []   # for 안에 넣으면 초기화돼서 밖으로 빼야함
def create_user(name, age, address):
    for i in range(0, 5):
        user_info = {}
        user_info['name'] = name[i]
        user_info['age'] = age[i]
        user_info['address'] = address[i]
        print(f'{name[i]}님 환영합니다!')
        many_user.append(user_info)
        
create_user(name, age, address)    

number_of_book = 100

def decrease_book(book_num):
    global number_of_book
    number_of_book -= book_num
    print(f'남은 책의 수 : {number_of_book}')


info = dict(map(lambda x: (x['name'], x['age']), many_user))

def rental_book(info):
    for j in info:
        decrease_book(info[j] // 10)
        print(f'{j}님이 {int(info[j]) // 10}권의 책을 대여하였습니다.')
    return ''

map(print(end=''), rental_book(info))   # 야매 ???


''' 참고하기 (호성님코드)
number_of_people = 0


def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


many_user = []   # for 안에 넣으면 초기화돼서 밖으로 빼야함
def create_user(name, age, address):
    for i in range(0, 5):
        user_info = {}
        user_info['name'] = name[i]
        user_info['age'] = age[i]
        user_info['address'] = address[i]
        print(f'{name[i]}님 환영합니다!')
        many_user.append(user_info)

create_user(name, age, address)    

number_of_book = 100

def decrease_book(book_num):
    global number_of_book
    number_of_book -= book_num
    


info = dict(map(lambda x: (x['name'], x['age']), many_user))
def rental_book(name_age):
    name, age = name_age
    result = []
    remain_book = []
    decrease_book(age//10)
    remain_book.append(f'남은 책의 수 : {number_of_book}')
    result.append(f'{name}님이 {age//10}권의 책을 대여하였습니다.')

    return remain_book, result
    

final_result = list(map(rental_book, info.items()))
for i in final_result:
    print(str(i[0][0]))
    print(str(i[1][0]))
'''
