# 미로 탐색
import sys
min_cnt = float('inf')
def find(start, cnt = 1):
    global min_cnt
    (sx, sy) = start
    if cnt >= min_cnt:
        return
    if start == (M-1, N-1):
        if cnt < min_cnt:
            min_cnt = cnt
            return
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]
        if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 1: # 이동 가능
            next = (nx, ny)  # 이동
            arr[ny][nx] = 0 # 방문 표시
            find(next, cnt+1) # 또 다음 노드 찾으러
            arr[ny][nx] = 1 # 초기화

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
find((0,0))
print(min_cnt)