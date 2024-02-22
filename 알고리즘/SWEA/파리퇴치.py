# 파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 누적합 2차원 리스트
    sum_arr = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            sum_arr[i][j] += arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

    max_v = 0
    for i in range(M, N+1):
        for j in range(M, N+1):
            val = sum_arr[i][j] - sum_arr[i-M][j] - sum_arr[i][j-M] + sum_arr[i-M][j-M]
            max_v = max(val, max_v)
    print(f'#{tc} {max_v}')
