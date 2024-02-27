# 크리스마스 선물 14235
import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    p = list(map(int, input().split()))
    if p[0] == 0: # 아이 만남
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(-1)
    else: # 선물 충전
        for i in range(1, len(p)):
            heapq.heappush(arr, -p[i])