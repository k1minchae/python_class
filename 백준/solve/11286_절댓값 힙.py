# 절댓값 힙
import sys
import heapq
input = sys.stdin.readline
arr = []
min_cnt = {}
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if arr:
            A = heapq.heappop(arr)
            if min_cnt.get(A, 0) > 0:
                print(-A)
                min_cnt[A] -= 1
            else:
                print(A)
        else:
            print(0)
    else:
        if x < 0:
            heapq.heappush(arr, -x)
            min_cnt[-x] = min_cnt.get(-x, 0) + 1
        if x > 0:
            heapq.heappush(arr, x)
