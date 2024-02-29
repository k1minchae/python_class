# 양봉업자 코코
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0


    def bee(y, x, cnt, val):
        global max_val
        if 0 > y or 0 > x or y >= N or x >= M or arr[y][x] == 0:
            return
        if cnt == 4:
            max_val = max(val + arr[y][x], max_val)
            return
        honey = arr[y][x]
        arr[y][x] = 0
        bee(y + 1, x, cnt + 1, val + honey)
        bee(y - 1, x, cnt + 1, val + honey)
        bee(y, x - 1, cnt + 1, val + honey)
        bee(y, x + 1, cnt + 1, val + honey)

        if x % 2 == 0:  # 짝수면 위 대각선도 됨
            bee(y - 1, x + 1, cnt + 1, val + honey)
            bee(y - 1, x - 1, cnt + 1, val + honey)
        else:  # 홀수면 아래 대각선도 됨
            bee(y + 1, x - 1, cnt + 1, val + honey)
            bee(y + 1, x + 1, cnt + 1, val + honey)

        arr[y][x] = honey


    def cross_T(y, x):  # t모양 찾기
        global max_val
        val = 0
        if x % 2:  # 홀수
            val_1 = arr[y][x]
            val_2 = arr[y][x]
            dir_1 = [(0, -1), (1, 0), (0, 1)]
            dir_2 = [(1, -1), (1, 1), (-1, 0)]
            for d in range(3):
                ny = dir_1[d][0] + y
                nx = dir_1[d][1] + x
                if 0 <= ny < N and 0 <= nx < M:
                    val_1 += arr[ny][nx]
                else:
                    val_1 = 0

            for d in range(3):
                ny = dir_2[d][0] + y
                nx = dir_2[d][1] + x
                if 0 <= ny < N and 0 <= nx < M:
                    val_2 += arr[ny][nx]
                else:
                    val_2 = 0
            val = max(val_1, val_2)

        else:  # 짝수
            val_1 = arr[y][x]
            val_2 = arr[y][x]
            dir_1 = [(-1, -1), (1, 0), (-1, 1)]
            dir_2 = [(0, -1), (0, 1), (-1, 0)]
            for d in range(3):
                ny = dir_1[d][0] + y
                nx = dir_1[d][1] + x
                if 0 <= ny < N and 0 <= nx < M:
                    val_1 += arr[ny][nx]
                else:
                    val_1 = 0

            for d in range(3):
                ny = dir_2[d][0] + y
                nx = dir_2[d][1] + x
                if 0 <= ny < N and 0 <= nx < M:
                    val_2 += arr[ny][nx]
                else:
                    val_2 = 0
            val = max(val_1, val_2)

        max_val = max(val, max_val)


    for i in range(N):
        for j in range(M):
            bee(i, j, 1, 0)
            cross_T(i, j)
    print(f'#{tc} {max_val}')