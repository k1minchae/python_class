# 미로(백트래킹)
def backtracking(s, e):
    global result
    if s == e:
        result = 1
        return

    for d in range(4):
        nx = s[0] + dx[d]
        ny = s[1] + dy[d]
        next = (nx, ny)

        if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == 0:
            arr[ny][nx] = 1
            backtracking(next, e)
            arr[ny][nx] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    visited = []
    start = ()
    end = ()
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (j, i)
            elif arr[i][j] == 3:
                arr[i][j] = 0
                end = (j, i)
            if start and end:
                break

    backtracking(start, end)
    print(f'#{tc} {result}')
