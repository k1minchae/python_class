# 이사(mid)
from collections import deque
def BFS(G):
    global result
    visited = [0] * N
    q = deque()
    q.append(R-1)
    visited[R-1] = 1
    while q:
        v = q.popleft()
        if v == G:
            if visited[v] <= K+1:
                result += 1
            return
        for next in arr[v]:
            if visited[next]==0:
                q.append(next)
                visited[next] = visited[v] + 1

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
R, K = map(int, input().split())
result = 0

for i in range(N):
    BFS(i)
print(result)