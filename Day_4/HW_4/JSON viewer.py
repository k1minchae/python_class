import requests

dummy_data = []


for i in range(1, 11):  # URL 은 무작위 유저 API
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}').json()
    dummy_data.append(response['name'])

print(dummy_data)