import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [[0 for _ in range(N)] for _ in range(N)]

def f(s):
    q = deque([s])
    visited = [0] * N
    while q:
        v = q.popleft()
        for w in range(N):
            if arr[v][w] and not visited[w]:
                result[s][w] = 1
                visited[w] = 1
                q.append(w)
    return

for i in range(N):
    f(i)

for i in result:
    print(*i)