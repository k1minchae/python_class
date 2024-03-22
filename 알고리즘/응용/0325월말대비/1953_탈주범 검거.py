# 탈주범 검거
from collections import deque
def BFS(sy, sx):
    q = deque([(sy, sx, arr[sy][sx])])
    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1

    while q:
        y, x, tur = q.popleft()
        for dy, dx in dir[tur]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and arr[ny][nx] != '0':
                if dy == -1 and (arr[ny][nx] == '3' or arr[ny][nx] == '4' or arr[ny][nx] == '7'):
                    continue
                if dy == 1 and (arr[ny][nx] == '3' or arr[ny][nx] == '5' or arr[ny][nx] == '6'):
                    continue
                if dx == 1 and (arr[ny][nx] == '2' or arr[ny][nx] == '4' or arr[ny][nx] == '5'):
                    continue
                if dx == -1 and (arr[ny][nx] == '2' or arr[ny][nx] == '6' or arr[ny][nx] == '7'):
                    continue
                q.append((ny, nx, arr[ny][nx]))
                visited[ny][nx] = visited[y][x] + 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 1 <= visited[i][j] <= L :
                cnt += 1
    return cnt

dir = {
    '1': [(-1, 0), (1, 0), (0, -1), (0, 1)],
    '2': [(-1, 0), (1, 0)],
    '3': [(0, -1), (0, 1)],
    '4': [(-1, 0), (0, 1)],
    '5': [(1, 0), (0, 1)],
    '6': [(1, 0), (0, -1)],
    '7': [(-1, 0), (0, -1)]}

T = int(input())
for tc in range(1, T+1):
    N, M, sy, sx, L = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]

    print(f'#{tc}', BFS(sy, sx))