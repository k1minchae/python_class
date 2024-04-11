# 방탈출
import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_val = 0
max_d = 0
def bfs(sy, sx):
    global max_val, max_d
    q = deque([(sy, sx)])
    visited = [[-1] * M for _ in range(N)]
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1 and arr[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                if max_d < visited[ny][nx]:
                    max_d = visited[ny][nx]
                    max_val = arr[ny][nx] + arr[sy][sx]
                elif max_d == visited[ny][nx]:
                    max_val = max(max_val, arr[ny][nx] + arr[sy][sx])
                q.append((ny, nx))

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            bfs(i, j)
print(max_val)