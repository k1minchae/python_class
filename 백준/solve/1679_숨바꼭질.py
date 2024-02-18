# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
visited = [0] * 100001

def BFS():
    visited[N] = 1
    q = deque([N])
    while q:
        v = q.popleft()
        if v == K:
            return visited[v] - 1
        for next in [v + 1, v - 1, 2 * v]:
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = visited[v] + 1
                q.append(next)
print(BFS())