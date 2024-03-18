# 욕심쟁이 판다
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DP = [[0] * n for _ in range(n)]

def DFS(sy, sx, cnt=1):
    eat = arr[sy][sx]
    arr[sy][sx] = 0
    max_cnt = cnt  # 현재 위치에서의 최대 대나무 개수
    for dy, dx in dirs:
        ny = dy + sy
        nx = dx + sx
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > eat:
            max_cnt = max(max_cnt, DFS(ny, nx, cnt + 1))
    arr[sy][sx] = eat
    return max_cnt  # 최대 대나무 개수 반환

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, DFS(i, j))
print(result)