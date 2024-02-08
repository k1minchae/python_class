# 소수점 아래 N번째 수 구하기
import sys
from decimal import Decimal, getcontext, ROUND_DOWN
A, B, N = map(int, sys.stdin.readline().split())
getcontext().prec = N+1
getcontext().rounding = ROUND_DOWN
number = str(Decimal(A) / Decimal(B)).split('.')
if len(number) == 1:
    print(0)

else:
    if len(number[1]) < N:
        print(0)
    else:
        print(number[1][N-1])