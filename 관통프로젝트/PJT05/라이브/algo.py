import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [(0, 0)]
for _ in range(M):
    x = tuple(map(int, input().split())) # 날짜, 페이지
    arr.append(x)
dp = [[0] * (M+1) for _ in range(N+1)]

for j in range(1, M+1): # 챕터
    for i in range(1, N+1): # 날짜
        day = arr[j][0]
        if day > i:
            dp[i][j] = dp[i][j-1]
            continue
        page = arr[j][1]
        dp[i][j] = max(dp[i][j-1], dp[i-day][j-1] + page)
print(dp[N][M])