import sys

T = int(input())

for i in range(1, T+1):
    TC = int(input())
    students = list(map(int, sys.stdin.readline().split()))    
    dict_students = {}
    for j in students:
        dict_students[j] = dict_students.get(j, 0) + 1

    max_value = max(dict_students.values())
    max_count = []

    for key, value in dict_students.items():
        if value == max_value:
            max_count.append(key)
    

    print(f'#{i} {max(max_count)}')


