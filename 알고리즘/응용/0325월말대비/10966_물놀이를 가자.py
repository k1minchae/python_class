# 물놀이를 가자
from collections import deque
def BFS(sy, sx):
    q = deque([(sy, sx)])
    visited = [[-1] * M for _ in range(N)]
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if arr[y][x] == 'W':
            return visited[y][x]
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                continue
            if arr[i][j] == 'L':
                result += BFS(i, j)
    print(f'#{tc}', result)