# 정사각형 방
def dfs(y, x, start, cnt=1):
    global max_cnt, room
    if cnt > max_cnt:
        max_cnt = cnt
        room = start
    elif cnt == max_cnt:
        room = min(start, room)

    for dy, dx in dir:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == arr[y][x] + 1:
            dfs(ny, nx, start, cnt + 1)

T = int(input())
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 1
    room = N**2
    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j])
    print(f'#{tc}', room, max_cnt)