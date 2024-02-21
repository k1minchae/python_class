# 동전 0
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if values[i] > K:
        continue
    else:
        coin = K // values[i]
        K -= coin * values[i]
        cnt += coin
print(cnt)