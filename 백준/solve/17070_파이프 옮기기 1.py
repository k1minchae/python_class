# 파이프 옮기기 1
import sys
input = sys.stdin.readline
import pprint
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N+1)] for _ in range(N+1)] # [가로, 세로, 대각]
dp[1][2][0] = 1 # 처음에 가로로 놓여있음

for i in range(1, N+1):
    for j in range(2, N+1):
        if arr[i-1][j-1] == 1: # 현재 놓으려는 자리가 벽일 경우 pass
            continue
        # (가로 -> 가로 경우의수) + (대각 -> 가로 경우의수)로 dp 갱신
        dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][0] + dp[i][j-1][2])
        # (세로 -> 세로 경우의수) + (대각 -> 세로 경우의수)로 갱신
        dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1] + dp[i-1][j][2])
        # 대각일때는 벽을 긁을 수 있는 경우를 걸러줘야함
        if arr[i-2][j-1] == 1 or arr[i-1][j-2] == 1:
            continue
        # 대각일땐 가로, 세로, 대각 다 되므로 세 경우의수를 다 더해준 값으로 dp갱신
        dp[i][j][2] = max(dp[i][j][2], dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2])
# pprint.pprint(dp)
print(sum(dp[N][N]))
