T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    DP = [[0] * (N + 1) for _ in range(2)]

    if N == 1:
        print(max(arr[0][0], arr[1][0]))
        continue

    DP[0][1] = arr[0][0]
    DP[1][1] = arr[1][0]

    for j in range(2, N + 1):
        DP[0][j] = max(DP[1][j - 1], DP[1][j - 2]) + arr[0][j - 1]
        DP[1][j] = max(DP[0][j - 1], DP[0][j - 2]) + arr[1][j - 1]

    print(max(DP[0][N], DP[1][N]))
