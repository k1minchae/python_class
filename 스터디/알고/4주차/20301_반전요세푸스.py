# 반전 요세푸스
import sys

N, K, M = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N+1)]
result = []
cnt = 0
is_reverse = False
curr_idx = 0
while arr:
    if cnt == M:
        cnt = 0
        is_reverse = not is_reverse
    if not is_reverse:
        del_idx = (curr_idx + K-1) % len(arr)
    else:
        del_idx = (curr_idx - K) % len(arr)
    cnt += 1
    result.append(arr[del_idx])
    del arr[del_idx]
    curr_idx = del_idx

print(*result, sep='\n')