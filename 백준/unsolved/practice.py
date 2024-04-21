# 과제
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
N = int(input())
arr = []
for _ in range(N):
    d, w = map(int, input().split())
    arr.append((d, w))
dp = [0] * 1001
arr.sort()
q = [arr[0][1]]
d = 2
for i in range(1, N):
    day = arr[i][0]
    score = arr[i][1]
    if day < d:
        q_score = heappop(q)
        if q_score > score:
            continue
        else:
            heappush(q, score)
    else:
        heappush(q, score)
        d += 1
print(sum(q))

