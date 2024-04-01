import sys

input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque([(0, 0, 0, 1)])  # 좌표 y, x, 벽을 부순 횟수, 거리
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # 벽을 부수고 방문한 경우와 아닌 경우 구분
    visited[0][0][0] = 1  # 시작점 방문 표시 (벽을 부수지 않음)

    while q:
        y, x, wall, dis = q.popleft()
        if y == N - 1 and x == M - 1:  # 도착지에 도달한 경우
            return dis

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == '0' and visited[ny][nx][wall] == 0:  # 벽이 아니고, 방문하지 않은 경우
                    visited[ny][nx][wall] = 1
                    q.append((ny, nx, wall, dis + 1))
                elif arr[ny][nx] == '1' and wall == 0 and visited[ny][nx][1] == 0:  # 벽이고, 벽을 부수지 않았으며, 방문하지 않은 경우
                    visited[ny][nx][1] = 1
                    q.append((ny, nx, 1, dis + 1))

    return -1  # 도착지에 도달할 수 없는 경우


dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

print(bfs())