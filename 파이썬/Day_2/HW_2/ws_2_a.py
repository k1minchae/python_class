'''
zero_list 변수에 숫자 0 을 하나 가지고 있는 리스트를 할당한다.
zero_list 변수를 출력한다.
many_zero_list 변수에 숫자 0을 25만개 가지고 있는 리스트를 할당한다.
numbers 변수에 range를 활용하여 1부터 10까지의 수를 가진 리스트를 할당한다.
numbers 변수를 출력한다.
numbers의 3번째부터 마지막 요소까지 출력한다.
'''

zero_list = [0]
print(zero_list)

many_zero_list = [0] * 250000
print(len(many_zero_list))

numbers = list(range(1, 11))    # range만쓰면 range가 출력된다.
print(numbers)
print(numbers[3:])