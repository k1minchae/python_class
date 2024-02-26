# 퍼펙트 셔플
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    S1 = deque(arr[:(N-1)//2+1])
    S2 = deque(arr[(N-1)//2 + 1:])
    result = []
    while S1 or S2:
        if S1:
            result.append(S1.popleft())
        if S2:
            result.append(S2.popleft())
    print(f'#{tc}', *result)

'''
투포인트 알고리즘
a = 맨처음
b = 중간 + 1

반복문을 돌릴 때
a 출력 => a += 1
b 출력 => b += 1

'''
T = int(input())
N = 0
arr=[]

def get_result():
    a = 0
    b = (len(arr) + 1) // 2
    for turn in range(len(arr)):
        if turn % 2 == 0:
            print(arr[a], end =' ')
            a += 1
        else:
            print(arr[b], end = ' ')
            b += 1
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    print(f'#{tc}',end=' ')
    get_result()
    print()