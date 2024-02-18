# DFS 와 BFS
import sys
from collections import deque
input = sys.stdin.readline
N, M, S = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1    # 양방향

stack = []
visited_D = []
def DFS(s):
    stack.append(s)
    visited_D.append(s+1)
    while stack:
        v = stack.pop()
        for n in range(N):
            if arr[v][n] and n+1 not in visited_D:
                DFS(n)
    return

visited_B = [S]
def BFS(s):
    q = deque([s])
    while q:
        v = q.popleft()
        for w in range(N):
            if arr[v][w] and w+1 not in visited_B:
                q.append(w)
                visited_B.append(w + 1)
    return

DFS(S-1)
print(*visited_D)

BFS(S-1)
print(*visited_B)