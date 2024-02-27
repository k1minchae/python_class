# 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [0] * (N+1)
def BFS():
    q = deque([1])
    visited = [0] * (N+1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for w in adj[x]:
            if not visited[w]:
                parent[w] = x
                visited[w] = 1
                q.append(w)
    return
BFS()
print(*parent[2:], sep='\n')