# 카드 놓기
import sys
from collections import deque
input = sys.stdin.readline
from collections import deque
N = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1]
result = deque([])

for i in range(1, N+1):
    if arr[i-1] == 1:
        result.appendleft(i)
    elif arr[i-1] == 2:
        result.rotate(-1)
        result.appendleft(i)
        result.rotate(1)
    else:
        result.append(i)
print(*result)