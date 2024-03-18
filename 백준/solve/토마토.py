import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split()) # 가 세 높
arr = [list(map(int, input().split())) for _ in range(N*H)]

q = deque([])
for i in range(N*H):
    for j in range(M):
        # 익은 토마토 큐에 추가
        if arr[i][j] == 1:
            q.append([i, j, 0])    # 위치와 날짜

# 상하좌우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
if H != 1 : dir += [(-N, 0), (N, 0)]    # 높이가 1보다 크다면 아래 위 추가

def BFS():
    day = 0 # 0일로 시작
    while q:
        y, x, day = q.popleft()
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x

            # 상하좌우 검사
            if -1 <= dy <= 1:
                # y좌표가 해당 층을 벗어나지 않기 위해 범위설정
                start = y//N * N
                end = start + N
                if start > ny or end <= ny or 0 > nx or M <= nx:
                    continue

            # z 축 위 아래 검사
            else:
                if 0 > ny or ny >= N*H:
                    continue

            # 안익은 토마토 발견
            if arr[ny][nx] == 0:
                arr[ny][nx] = 1 # 익힌 뒤에
                q.append([ny, nx, day + 1]) # 큐에 추가

    for i in range(N*H):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
    return day

print(BFS())