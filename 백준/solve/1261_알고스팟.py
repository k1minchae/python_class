# 알고스팟
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split()) # 가로, 세로
arr = [list(input().rstrip()) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def bfs():
    visited = [[-1] * M for _ in range(N)] # 벽 부순 개수 저장할 배열
    visited[0][0] = 0 # 0개 부순 채로 시작
    q = deque([(0, 0)])

    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M: # 범위 안이어야 함
                # 부순 벽의 수 : wall
                if arr[ny][nx] == '1': wall = visited[y][x] + 1 # 벽이라면 + 1 하고,
                else: wall = visited[y][x] # 벽이 아니라면 유지

                # 아직 방문하지 않았거나 더 적게 부술수 있는 경우 갱신
                if visited[ny][nx] == -1 or visited[ny][nx] > wall:
                    q.append((ny, nx))
                    visited[ny][nx] = wall

    return visited[N-1][M-1]

print(bfs())