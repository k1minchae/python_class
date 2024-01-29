# my_len 만들기
my_list = [4, 5, 12, 6, 8]
def my_len(list):
    count = 0
    for i in my_list:
        count += 1
    return count
print(my_len(my_list))

# my_max 만들기
def my_max(list):
    x = list[0]
    for j in my_list:
        if j > x:
            x = j
    return x
print(my_max(my_list))

# my_min 만들기
def my_min(list):
    y = list[0]
    for k in my_list:
        if k < y:
            y = k
    return y
print(my_min(my_list))

# my_sum 만들기
def my_sum(list):
    z = 0
    for l in my_list:
        z += l
    return z
print(my_sum(my_list))

# my_sort 만들기
def my_sort(list):
    for q in range(len(list)):
        for w in range(len(list)-1):
            if list[w] > list[w+1]:
                list[w], list[w+1] = list[w+1], list[w]
    return list
print(my_sort(my_list))



# 재귀함수
# 1. 팩토리얼
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
print(fac(10))

# 2. 피보나치 수열
def fib(num):
    if num <= 2:
        return 1
    elif num ==0:
        return 0
    return fib(num-1) + fib(num-2)
print(fib(7))

# 3. 거듭제곱 계산
def square(x, y):
    if y == 0:
        return 1
    else:
        return x * square(x, y-1)
print(square(2, 3))

# 문자열 뒤집기
msg = 'Hello'
def reverse_string(string):
    if len(string) ==1:
        return string
    return reverse_string(string[1:]) + string[0]
print(reverse_string(msg))


# 2차원 리스트
# 1. 행렬 뒤집기
list_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
def flip(list):
    for e in range(len(list)):
        if e == 0:
            list[e], list[len(list)-1] = list[len(list)-1], list[e]
        elif e == len(list) -2:
            break
        else:
            list[e], list[e+1] = list[e+1], list[e]

    for inner_list in list:
        for t in range(len(inner_list)):
            if t == 0:
                inner_list[0], inner_list[len(inner_list)-1] = inner_list[len(inner_list)-1], inner_list[0]
            elif t == len(inner_list) -2:
                break
            else:
                inner_list[e], inner_list[e+1] = inner_list[e+1], inner_list[e]
    return list
print(flip(list_2))

# 2. 행렬의 합
list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
list2 = [
    [2, 4, 6],
    [3, 6, 9],
    [1, 3, 5]
]

def plus(list_a, list_b):
    for rows in range(len(list_a)):
        for cols in range(len(list_a[rows])):
            list_a[rows][cols] += list_b[rows][cols]
    return list_a
print(plus(list1, list2))

unsorted= [324, 5, 3]
unsorted.sort()
print(unsorted)