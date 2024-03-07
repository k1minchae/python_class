# 2×n 타일링
import sys
input = sys.stdin.readline
n = int(input())
DP = [0] * (n+1)
DP[1] = 1
if n >= 2:
    DP[2] = 2
def f(x):
    if x >=2 and DP[x] == 0:
        DP[x] = f(x-1) + f(x-2)
    return DP[x]
f(n)
print(DP[n] % 10007)