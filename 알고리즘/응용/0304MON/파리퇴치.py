# 파리퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dir_cross = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    max_kill = 0
    for i in range(N):
        for j in range(N):
            kill_plus = arr[i][j]   # 십자가 모양
            kill_cross = arr[i][j]  # 대각선 모양
            for dy, dx in dir:
                for p in range(1, M):
                    ny = i + dy * p
                    nx = j + dx * p
                    if 0 <= ny < N and 0 <= nx < N:
                        kill_plus += arr[ny][nx]

            for dy, dx in dir_cross:
                for p in range(1, M):
                    ny = i + p * dy
                    nx = j + p * dx
                    if 0 <= ny < N and 0 <= nx < N:
                        kill_cross += arr[ny][nx]
            max_kill = max(kill_plus, kill_cross, max_kill)

    print(f'#{tc} {max_kill}')