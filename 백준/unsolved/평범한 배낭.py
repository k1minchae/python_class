# 평범한 배낭
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # [무게, 가치]

# 세로축 : 담을 수 있는 무게, 가로축 : 지금 확인하고 있는 물건의 idx
dp = [[0] * N for _ in range(K+1)]
# 첫 번째 물건 담아놓고 시작
for i in range(arr[0][0], K+1):
    dp[i][0] = arr[0][1]

for idx in range(1, N): # 지금 확인하는 물건의 idx
    for max_w in range(1, K+1): # 가방의 최대 무게
        weight = arr[idx][0] # 현재 물건의 무게
        val = arr[idx][1] # 현재 물건의 가치
        if max_w < weight:
            dp[max_w][idx] = dp[max_w][idx-1]
        else:
            # 해당 물건 넣었을 때의 값
            put_in = val + dp[max_w-weight][idx-1]

            # 해당 물건 넣었을 때의 값 vs 안 넣었을 때의 값 비교해서 최대값으로 저장
            dp[max_w][idx] = max(put_in, dp[max_w][idx-1])
print(dp[K][N-1])

