# 리모컨
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
if M:
    broken = list(input().split())
else:
    broken = []

# +와 -로만 이동했을 때의 횟수를 최대값으로 설정해둠
min_cnt = abs(N-100)

# 최대로 누를 수 있는 숫자 : 백만
# 리모콘으로 누를 수 있는 모든 경우의 수 확인
for num in range(1000001):
    for n in str(num):
        # 누를 수 없는 번호일 때
        if n in broken:
            break

    # 누를 수 있는 번호일 때만 횟수 계산
    else:
        # 번호 누른 수와 (+, -) 누른 수를 더함
        cnt = len(str(num)) + abs(num-N)
        min_cnt = min(cnt, min_cnt)

print(min_cnt)