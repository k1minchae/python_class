# 최소 힙
import heapq
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)