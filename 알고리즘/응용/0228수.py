# arr = ['A', 'B', 'C']
# n = len(arr)
#
# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:   # 1비트가 1인지 확인
#             # 1이 아니라면 False, 1 이라면 True
#             print(arr[i], end =' ')
#         tar >>= 1   # 검사한 자리는 오른쪽으로 밀어서 제거
#     print()
#
# for j in range(1 << n):
#     get_sub(j)
'''
도전 과제
친구와 카페 방문

민철이는 친구 {A, B, C, D, E} 가 있다.
이 중 최소 2명 이상의 친구를 선정하여 함께 카페에 가려고 한다.

총 몇가지의 경우가 가능할까?

arr = ["A", "B", "C", "D", "E"]
n = len(arr)

def friends(target):
    cnt = 0
    for i in range(n):
        # 1비트가 1인지 확인하는 코드
        if target & 0x1:
            cnt += 1    # 명 수 카운트
        # right shift 비트 연산자 사용 -> 오른쪽 끝 비트를 하나씩 제거
        target >>= 1
    return cnt

result = 0
for tar in range(1 << n):
    if friends(tar) >= 2:  # 비트가 2개 이상 1이라면 (2명 이상)
        result += 1
print(result)
'''

# arr = ['A', 'B', 'C', 'D', 'E']
# for a in range(5):
#     for b in range(a+1, 5):
#         for c in range(b+1, 5):
#             print(arr[a], arr[b], arr[c])
'''
A B C
A B D
A B E
A C D
A C E
A D E
B C D
B C E
B D E
C D E
'''

# arr = ['A', 'B', 'C', 'D', 'E']
# path = []
#
# n = 3
# def run(level=0, start=0):
#     if level == n:
#         print(*path)
#         return
#
#     for i in range(start, 5):
#         path.append(arr[i])
#         run(level+1, i+1)
#         path.pop()
# run()

'''
A B C
A B D
A B E
A C D
A C E
A D E
B C D
B C E
B D E
C D E
'''
# path = []
# def dice(level = 0, start = 1):
#     if level == 3:
#         print(*path)
#         return
#     for i in range(start, 7):
#         path.append(i)
#         # 현재 뽑은 수보다 크거나 같은 다음수를 뽑는다
#         dice(level + 1, i)  # start 대신 i
#         path.pop()
# dice()
'''
arr = [15, 30, 50, 10]
arr.sort(reverse=True)
sum_time = 0

while arr:
    t = arr.pop()
    sum_time += t * len(arr)
print(sum_time)
'''

# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# n = len(arr)
#
# def sub(tar):
#     sum_v = 0
#     temp = []
#     for i in range(n):
#         if tar & 0x1:
#             sum_v += arr[i]
#             temp.append(arr[i])
#         tar >>= 1
#     if sum_v == 0:
#         print(temp)
#     return
#
# for j in range(1, 1 << n):
#     sub(j)

'''
[3, -9, 6]
[-1, 3, -9, 7]
[6, -6]
[-1, 7, -6]
[-1, 3, -9, 6, 7, -6]

~중략~

[-1, -6, 5, 4, -2]
[-1, 3, -9, 6, -6, 5, 4, -2]
[-9, 7, -6, 1, 5, 4, -2]
'''