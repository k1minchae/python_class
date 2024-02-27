# 1049 : 기타줄 (31120/ 40)
import sys
N, M = map(int, sys.stdin.readline().split())
one_p = set_p = float('inf')
total_p = 0

for _ in range(M):
    sp, op = map(int, sys.stdin.readline().split())
    if sp < set_p:
        set_p = sp
    if op < one_p:
        one_p = op

if one_p * 6 <= set_p:
    total_p = one_p * N
else:   # 세트가 더 싼 경우
    if set_p < (N % 6) * one_p: # 6개 미만도 세트가 더 싼경우
        total_p = set_p * (N//6 + 1)
    else:
        total_p = set_p * (N//6) + one_p * (N % 6) # 6개미만 낱개 구매

print(total_p)
