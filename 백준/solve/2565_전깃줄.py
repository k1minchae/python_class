# 전깃줄
N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort() # 모든 전선들을 A 전봇대 기준으로 오름차순 정렬
dp = [1] * N # 최소값(1): 자기 자신만 연결되어 있는경우 로 dp리스트 초기화

for i in range(1, N): # A 전봇대 기준 i번째 전선
    for j in range(i):  # i번째 이전 전선들 확인
        if arr[i][1] > arr[j][1]: # 이전 전선의 끝점이 더 작다면  교차 X
        # 즉, j번째 전선에서의 최대값에 i번째를 더 연결할 수 있으므로 dp[j] + 1 이 dp[i] 값에 들어올 수 있게 된다.
        # 하지만 우리는 최대로 많이 연결할 수 있는걸 구할거라서, 이전에 갱신한 dp값과 비교한다.
            dp[i] = max(dp[i], dp[j]+1)
            # dp[i] 에는 i 번째 전깃줄을 살렸을 때의 연결가능한 전깃줄 개수의 최댓값이 저장된다

print(N - max(dp))