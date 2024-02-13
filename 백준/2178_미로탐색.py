# 미로 탐색
import sys

def find(start, cnt = 1):
    (sx, sy) = start
    if start == (M-1, N-1):
        return cnt
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]
        if 0 <= nx < N and 0 <= ny < M and arr[ny][nx] == 0:
            arr[ny][nx] = 1
            next = (nx, ny)
            result = find(next, cnt+1)
            if result is not None:
                return result
    return None
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

print(find((1, 1)))