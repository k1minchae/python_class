import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

zero = []   # 빈칸의 좌표 리스트
virus = []  # 바이러스의 좌표 리스트
visited = [[0] * M for _ in range(N)]  # 방문표시 할 리스트

# 바이러스 : 2, 벽: 1, 빈칸: 0
for i in range(N):
    for j in range(M):
        # 빈칸이면 -> 빈칸 좌표 저장
        if not arr[i][j]:
            zero.append((i, j))
        # 바이러스면 -> 방문표시 + 바이러스 좌표 저장
        if arr[i][j] == 2:
            virus.append((i, j))
            visited[i][j] = 1
        # 벽이면 -> 방문표시만
        if arr[i][j] == 1:
            visited[i][j] = 1

# 벽을 세울 수 있는 모든 경우의 수
wall_cases = list(combinations(zero, 3))
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상하좌우

def BFS(case, used):
    used = [row[:] for row in used]  # visited 리스트를 복사하여 사용
    q = deque(virus)    # 저장해둔 바이러스 리스트를 큐에 넣고 시작

    # 벽 세우기
    for cy, cx in case:
        used[cy][cx] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            # 벽, 바이러스를 다 방문처리 했으니깐 방문처리 안 된 곳은 무조건 빈칸
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                q.append((ny, nx))
                used[ny][nx] = 1

    # 큐가 비었을 때, 빈칸이 몇 갠지 센다
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not used[i][j]:
                cnt += 1
    return cnt

result = 0
for case in wall_cases:
    result = max(BFS(case, visited), result)
print(result)
