# 스터디 시간 정하기 1
import sys
input = sys.stdin.readline
N, T = map(int, input().split()) # 사람수, 스터디 시간
dp = [0] * 100002 # 계산의 편의를 위해 앞에 0 하나 추가
max_e = 0
for _ in range(N):
    K = int(input())
    for _ in range(K):
        S, E = map(int, input().split())
        # dp 맨앞에 [0] 추가했으므로 idx에 + 1해줌
        dp[S+1] += 1
        dp[E+1] -= 1 # 끝나는 시간은 스터디 시간에 포함 X
        # 탐색할 끝값 구하기
        max_e = max(E, max_e)

# 1부터 끝까지 dp배열 스위핑
# 예제 1에 대한 스위핑 결과값 : [0, 1, 2, 2, 1, 3, 3, 1, 2, 2, 1, 1, 1]
# 해당 시간에 스터디 가능한 사람 수를 구해줌
for i in range(1, max_e+1):
    dp[i] += dp[i-1]

# 슬라이딩 윈도우로 누적합의 최대를 구한다
start = 1
end = 1 + T

# 초기 sum값 (1부터 계산)
sum_v = sum(dp[start:end])
max_sum = sum_v # 초기값으로 max_sum 초기화
result = (0, T) # 초기값은 편의상 1, 1+T로 구하고있지만 원래는 0, T임

while end <= max_e + 1: # 누적합 계산
    sum_v -= dp[start] # 맨 앞 값 빼주고
    sum_v += dp[end] # 끝값 더해주고
    start += 1 # start, end값도 더해줌
    end += 1
    if max_sum < sum_v: # 최댓값 갱신이 된다면
        result = (start-1, end-1) # 결과 업데이트 (맨처음에 dp배열에 + 1 했으니깐 -1해줘야함)
        max_sum = sum_v
print(*result)