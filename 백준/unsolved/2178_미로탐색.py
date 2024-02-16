# 미로 탐색
import sys
from collections import deque
def BFS():
    visited[0][0] = 1
    q = deque([(0, 0)])   # y, x
    while q:
        (i, j) = q.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j]
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1 + visited[i][j]
                q.append((ny, nx))
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0 for _ in range(M)] for _ in range(N)]
print(BFS())