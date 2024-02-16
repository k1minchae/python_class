# 미로의 거리
from collections import deque
def BFS():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    visited[start_y][start_x] = 1
    q.append((start_x, start_y))

    while q:
        (x, y) = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                if arr[ny][nx] == '3':
                    return visited[y][x] - 1
                if arr[ny][nx] == '0':
                    q.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start_x = j
                start_y = i

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = BFS()
    print(f'#{tc} {result}')
