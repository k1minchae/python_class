# 다중상속 실습

# class Car:
#     def __init__(self, model):
#         self.model = model

# class Hyundai(Car):
#     color = "white"

#     def speed(self):
#         return "30km/h"
    
# class Kia(Car):
#     color = "black"

#     def engine(self):
#         return "1.6 turbo"

# class CarDrive(Hyundai, Kia):
#     def speed(self):
#         return "50km/h"
    
#     def power(self):
#         return '1,999cc'

# car = CarDrive('Sonata')
# print(car.speed())  # 50km/h -> 본인 method
# print(car.color)    # White -> Hyundai 에서 상속받은것



# 가장 많이 보게 될 예외 3가지
# NameError : 변수를 초기화 안했거나, 지역변수의 위치 잘못됨
# TypeError : 
# IndexError : 인덱스 범위 벗어남

def calculate_sum(a, b):
    return a + b
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    result = calculate_sum(result, numbers[i])

print(result) 

def my_view(reques, post_id):
    try:
        # post id 에서 해당하는 포스트를 가져오는 로직 수행
    except Post.DesNotExist:
        # 만약 포스트가 존재하지 않는경우 404 에러발생 -> 예외처리
        return '해당 포스트를 찾을 수 없습니다.'
    
    return render()