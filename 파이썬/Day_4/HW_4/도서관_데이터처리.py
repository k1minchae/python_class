
import requests

dummy_data = []

for i in range(1, 11):
    data = requests.get(f"https://jsonplaceholder.typicode.com/users/{i}").json()
    dummy_data.append({'company': data['company']['name']})

    # -80 < lat(위도) lng(경도) <80 인 경우 삽입
    if (-80 < float(data["address"]['geo']['lat']) < 80) and (-80 < float(data["address"]['geo']['lng']) < 80):
        dummy_data.append({'lat': data['address']['geo']['lat']})
        dummy_data.append({'lng': data['address']['geo']['lng']})
    elif (-80 < float(data["address"]['geo']['lat'])) < 80:
        dummy_data.append({'lat': data['address']['geo']['lat']})
    elif -80 < float(data["address"]['geo']['lng']) < 80:
        dummy_data.append({'lng': data['address']['geo']['lng']})

    dummy_data.append({'name': data['name']})

print(dummy_data)