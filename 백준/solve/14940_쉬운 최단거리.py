# 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            startx = j
            starty = i
            break

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[-1] * m for _ in range(n)]

def BFS():
    q = deque([[starty, startx]])
    visited[starty][startx] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1 and arr[ny][nx]:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
BFS()
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1 and not arr[i][j]:
            visited[i][j] = 0
    print(*visited[i])