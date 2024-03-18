# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

sy , sx = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sy = i
            sx = j
            break
    break

dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
max_time = 0
def bfs(sy, sx, size = 2, eat = 0):
    global max_time
    q = deque([(sy, sx, size, 0)])
    arr[sy][sx] = 0
    time = 0
    size = 2
    y, x = 0, 0
    while q:
        y, x, size, eat = q.popleft()
        if eat == size:
            size += 1
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx]:
                if arr[ny][nx] < size:
                    q.append((ny, nx, size, eat + 1))
                    arr[ny][nx] = 0
                elif arr[ny][nx] == size:
                    q.append((ny, nx, size, eat))
                time += 1

    fishes = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and arr[i][j] < size:
                dis = abs(i - y) + abs(j - x)
                fishes.append((dis, i, j))

    if not fishes:
        max_time = max(time, max_time)
        return max_time
    fishes.sort(key=lambda x: (x[0], x[2], x[1]))
    bfs(fishes[0][1], fishes[0][1], size, eat)
print(bfs())

