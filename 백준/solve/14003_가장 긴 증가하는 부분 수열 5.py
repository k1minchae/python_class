# 가장 긴 증가하는 부분 수열 5
import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

# 최장 부분수열의 길이 구하기
lis = []
pos = [0] * N
for i in range(N):
    idx = bisect_left(lis, arr[i])
    if len(lis) <= idx:
        lis.append(arr[i])
    else:
        lis[idx] = arr[i]
    pos[i] = idx # pos 에 LIS 길이 저장

# 역순으로 탐색하면서 실제 LIS 찾아내기
ans = []
lis_len = len(lis) - 1
for i in range(N-1, -1, -1):
    if pos[i] == lis_len:
        ans.append(arr[i])
        lis_len -= 1

print(len(ans))
print(*sorted(ans))