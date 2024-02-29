# 구슬 탈출 2
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # y, x

def BFS(sy, sx):
    q = deque([[sy, sx, 0]])
    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1
    min_cnt = 10 ** 6
    while q:
        y, x, cnt = q.popleft()
        if arr[y][x] == 'O':
            min_cnt = min(cnt, min_cnt)
        for d in range(4):
            for k in range(N-1, 0, -1):
                ny = y + dir[d][0] * k
                nx = x + dir[d][1] * k
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and (arr[ny][nx] == 'O' or arr[ny][nx] == '.'):
                    q.append([ny, nx, cnt+1])
    return min_cnt

def find():
    r_val = 10 ** 6
    b_val = 10 ** 6
    for i in range(N):
        for j in range(M):
            if r_val != 10 ** 6 and b_val != 10 ** 6:
                if r_val <= b_val:
                    return -1
                else:
                    return r_val
            if arr[i][j] == 'R':
                r_val = BFS(i, j)
            if arr[i][j] == 'B':
                b_val = BFS(i, j)

print(find())