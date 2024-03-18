import sys
input = sys.stdin.readline
import heapq
T = int(input())
for _ in range(T):
    k = int(input())
    max_q = []
    min_q = []
    arr = {}
    for _ in range(k):
        s, n = input().split()
        if s == 'I':
            n = int(n)
            arr[n] = arr.get(n, 0) + 1
            heapq.heappush(min_q, n)
            heapq.heappush(max_q, -n)
        elif s == 'D':
            if n == '1':
                while max_q:
                    x = heapq.heappop(max_q)
                    if arr.get(-x):
                        arr[-x] -= 1
                        break

            elif n == '-1':
                while min_q:
                    x = heapq.heappop(min_q)
                    if arr.get(x):
                        arr[x] -= 1
                        break

    max_v = float('-inf')
    min_v = float('inf')
    for keys, val in arr.items():
        if val:
            max_v = max(keys, max_v)
            min_v = min(keys, min_v)
    if max_v == float('-inf'):
        print('EMPTY')
    else:
        print(max_v, min_v)

