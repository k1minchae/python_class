# 한수 2
import sys
N = int(sys.stdin.readline())
dp = [0] * (N+1)

if N > 99:
    if N < 111:
        print(99)
    else:
        for i in range(100, N+1):
            if not dp[i]:
                x = 0
                while True:
                    ni = N

else:
    print(N)