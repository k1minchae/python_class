import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cross1 = [0] * (2 * (N-1) + 1) # 우상향 대각선
cross2 = [0] * (2 * (N-1) + 1) # 우하향 대각선
can = [] # 비숍을 놓을 수 있는 좌표들 모음
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1: # 가능한 좌표라면
            can.append((i, j)) # can 에 추가
max_cnt = 0
def dfs(y, x, i, cnt = 1):
    global max_cnt
    cross1[x+y] = 1 # 방문표시
    cross2[x+N-1-y] = 1
    for j in range(i+1, len(can)): # 다음 좌표로 이동
        ny = can[j][0]
        nx = can[j][1]
        if not cross1[ny+nx] and not cross2[nx+N-1-ny]: # 다음좌표에도 놓을 수 있다면 dfs
            dfs(ny, nx, j, cnt+1)
    cross1[x + y] = 0 # 백트래킹
    cross2[x + N - 1 - y] = 0
    max_cnt = max(cnt, max_cnt)
for i in range(len(can)):
    x = can[i][0]
    y = can[i][1]
    dfs(y, x, i)
print(max_cnt)