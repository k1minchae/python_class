# 정수 삼각형
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

DP = [[0] * (n+1) for i in range(1, n+1)]
DP[0][1] = arr[0][0]

if n > 1:
    DP[1][1] = arr[1][0] + DP[0][1]
    DP[1][2] = arr[1][1] + DP[0][1]

    if n > 2:
        for i in range(2, n):
            for j in range(1, i+2):
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + arr[i][j-1]


print(max(DP[n-1]))
