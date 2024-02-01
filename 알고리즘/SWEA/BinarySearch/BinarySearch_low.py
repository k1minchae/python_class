n = int(input())
arr = sorted(list(map(int, input().split()))) # 목록
k = int(input())
find_list = list(map(int, input().split())) # 찾아야 하는 수
result_list = []

def find_f(n, arr):
    start = 0
    end = n - 1
    while end >= start:
        middle = (start + end) // 2
        if find_num == arr[middle]:
            return 'O'
        elif find_num > arr[middle]:
            start = middle + 1
        elif find_num < arr[middle]:
            end = middle - 1
    return 'X'

for find_num in find_list:
    result = find_f(n, arr)
    result_list.append(result)


print(*result_list, sep = '')