# 스노우맨
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            startx = j
            starty = i
            break
visited = [[0] * M for _ in range(N)]

min_p = 10 ** 6
def BFS():
    global min_p
    q = deque([[starty, startx]])
    visited[starty][startx] = 1

    while q:
        sy, sx = q.popleft()
        if arr[sy][sx] == 3:
            min_p = min(min_p, visited[sy][sx])

        if sx + 1 < M and arr[sy][sx+1] and (not visited[sy][sx+1] or visited[sy][sx+1] > visited[sy][sx]):
            q.append([sy, sx+1])
            visited[sy][sx+1] = visited[sy][sx]

        if sx - 1 >= 0 and arr[sy][sx-1] and (not visited[sy][sx-1] or visited[sy][sx-1] > visited[sy][sx]):
            q.append([sy, sx-1])
            visited[sy][sx-1] = visited[sy][sx]

        up = 1
        while sy - up >= 0:
            ny = sy - up
            h_up = max(visited[sy][sx], up+1)
            if 0 <= ny < N and arr[ny][sx]:
                if not visited[ny][sx] or visited[ny][sx] > h_up:
                    visited[ny][sx] = h_up
                    q.append([ny, sx])
                break
            up += 1

        down = 1
        while sy + down < N:
            ny = sy + down
            h_down = max(visited[sy][sx], down + 1)
            if 0 <= ny < N and arr[ny][sx]:
                if not visited[ny][sx] or visited[ny][sx] > h_down:
                    visited[ny][sx] = h_down
                    q.append([ny, sx])
                break
            down += 1
    return min_p
print(BFS()-1)