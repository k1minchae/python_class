# 2638 치즈
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
time = 0

def bfs(sy, sx):
    global time
    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    arr[sy][sx] = 3 # 치즈를 녹일 수 있는 바깥공기
    cheese = []

    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if arr[ny][nx] == 0 or arr[ny][nx] == 3:
                    arr[ny][nx] = 3
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                else:
                    cheese.append((ny, nx))
                    visited[ny][nx] = 1

    if not cheese: # 이미 다 녹음
        return

    for y, x in cheese:
        cnt = 0
        for dy, dx in dir:
            cy = dy + y
            cx = dx + x
            if arr[cy][cx] == 3: # 바깥공기 카운트
                cnt += 1
        if cnt >= 2:
            arr[y][x] = 0
    time += 1
    return bfs(0, 0)

bfs(0, 0)
print(time)


