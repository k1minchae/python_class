import requests

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
    user_dict[f'{user["company"]["name"]}'] = [f'{user["name"]}']
    user_data.append(user_dict)  


censored_user_list = []

def create_user():
    for j in user_data:
        for name in j:
            if name not in black_list:
                censored_user_list.append(j)
    return censored_user_list



def censorship():
    for k in user_data:
        for l in k:
            if l in black_list:
                print(f'{l} 소속의 {k[f"{l}"]} 은/는 등록할 수 없습니다.')
            else:
                print('이상 없습니다.')


result = create_user()
censorship()
print(result)
