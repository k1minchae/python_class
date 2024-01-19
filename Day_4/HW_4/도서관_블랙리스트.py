import requests

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]
censored_user_list = {}
result = True

# def create_user():
#     for i in range(1, 11):
#         user_data = requests.get(f"https://jsonplaceholder.typicode.com/users/{i}").json()
#         if user_data['company']['name'] in black_list:
#             censored_user_list[user_data['company']['name']] = [user_data['name']]

for i in range(1, 11):
    user_data = requests.get(f"https://jsonplaceholder.typicode.com/users/{i}").json()
def create_user():
    censored_user_list[user_data['company']['name']] = [user_data['name']]

def censorship():
    for j in i:
        if j in black_list:
            create_user()
            return f'{회사명} 소속의 {사용자명} 은/는 등록할 수 없습니다.'
        else:
             return '이상 없습니다.'
       
censorship()

        

# GPT
# def create_user(user_data):
#     if result == False:
#         company_name = user_data["company"]["name"]
#         username = user_data["username"]
#         if company_name not in censored_user_list:
#             censored_user_list[company_name] = [username]

# def censorship():
#     global result
#     for j in user_list:
#         if j in black_list:
#             print(f'{j} 소속의 {str(censored_user_list.get(j, ""))} 은/는 등록할 수 없습니다.')
#             result = False
#             create_user({"company": {"name": j, "username": user_list[j][0]}})
#         else:
#             print('이상 없습니다.')
#             result = True
#             create_user({"company": {"name": j, "username": user_list[j][0]}})

# censorship()
# print(censored_user_list)