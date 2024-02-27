# 양봉업자 코코
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    def bee(y=0, x=0, cnt = 1, val = 0):
        global max_val
        if 0 > y or 0 > x or N <= y or M <= x:
            return
        if cnt == 4:
            max_val = max(val + arr[y][x], max_val)
            return

        honey = arr[y][x]
        arr[y][x] = 0
        bee(y+1, x, cnt+1, val + honey)
        bee(y-1, x, cnt+1, val + honey)
        bee(y, x+1, cnt+1, val + honey)
        bee(y, x-1, cnt+1, val + honey)
        arr[y][x] = honey


    for i in range(N):
        for j in range(M):
            bee(i, j)
    print(max_val)

