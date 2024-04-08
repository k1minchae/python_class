# ACM Craft
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    print(x)
    result = [0] * (N+1)
    result[x] = time[x-1]
    q = deque([x])
    while q:
        node = q.popleft()
        for next in adj[node]:
            result[next] += result[node] + time[next-1]
            q.append(next)
    print(result)
    return result[W]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    arr = [[]for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        adj[X].append(Y)
        arr[Y].append(X)
    W = int(input())
    min_t = 10 ** 6
    for n in range(1, N+1):
        if not arr[n]:
            min_t = min(bfs(n), min_t)
    print(min_t)