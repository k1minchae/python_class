import requests
import pprint

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


user_data = []  # userdata (이름:회사) 10개

for i in range(1, 11):
    user_dict = {}
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{i}").json()
    user_dict[f'{user["company"]["name"]}'] = f'{user["name"]}'
    user_data.append(user_dict)  


def create_user():
    for j in user_data:
        if j in black_list:

def censorship():
    pass
    for j in i:
        if j in black_list:
            create_user()
            return f'{회사명} 소속의 {사용자명} 은/는 등록할 수 없습니다.'
        else:
             return '이상 없습니다.'
       
result = create_user()
print(result)
