# 10844 : 쉬운 계단 수
N = int(input())
DP = [[0] * 10 for _ in range(101)]
# 자리수가 1일 때 가능한 것들
DP[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 2부터 N까지 가능한 것 모두 구하기
if N > 1:
    for r in range(2, N+1):
        for i in range(10):
            # 인접 숫자 추가
            if i-1 >= 0:
                DP[r][i] += DP[r-1][i-1]
            if i+1 < 10:
                DP[r][i] += DP[r-1][i+1]
print(sum(DP[N]) % 1000000000)
