# 치즈
import sys
input = sys.stdin.readline
from collections import deque
import pprint
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def BFS(sy, sx):
    global last_cheese, t
    t += 1
    cheese = 0
    visited = [[0] * M for _ in range(N)]
    arr[sy][sx] = 3 # 바깥 공기 3으로 표시
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and (not visited[ny][nx] or (visited[ny][nx] > visited[y][x] + 1)):
                if not arr[ny][nx] or arr[ny][nx] ==3: # 공기라면 바깥공기 표시
                    arr[ny][nx] = 3
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                else:
                    arr[ny][nx] = 0
                    visited[ny][nx] = 1
                    cheese += 1
    if cheese == 0:
        return
    last_cheese = cheese
    return BFS(0, 0)
last_cheese = 10 ** 6 # 녹인 치즈
t = 0
BFS(0,0)
print(t-1)
print(last_cheese)

