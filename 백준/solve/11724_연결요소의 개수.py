# 연결 요소의 개수
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0] * (N + 1)
result = 0
def BFS(s):
    q = deque([s])
    visited[s] = 1
    while q:
        x = q.popleft()
        for n in arr[x]:
            if not visited[n]:
                visited[n] = 1
                q.append(n)

for i in range(1, N+1):
    if not visited[i]:
        BFS(i)
        result += 1
print(result)
