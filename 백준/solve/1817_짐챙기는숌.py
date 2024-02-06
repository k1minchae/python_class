import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

space = 0
cnt = 0
for i in range(N):
    if space >= arr[i]:
        space -= arr[i]
    else:
        cnt += 1
        space = M - arr[i]
print(cnt)