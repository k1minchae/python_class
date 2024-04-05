# 회장뽑기
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N+1)]
result = {}
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    adj[a].append(b)
    adj[b].append(a)
def bfs(a):
    visited = [-1] * (N+1)
    visited[a] = 0
    q = deque([a])
    while q:
        x = q.popleft()
        if adj[x]:
            for n in adj[x]:
                if visited[n] == -1:
                    q.append(n)
                    visited[n] = visited[x] + 1
    score = max(visited)
    result[score] = result.get(score, []) + [a]
    return
for i in range(1, N+1):
    bfs(i)

min_k = 100000
val = []
for k, v in result.items():
    if min_k > k:
        min_k = k
        val = v

print(min_k, len(val))
print(*val)

