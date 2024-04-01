# 점수 계산
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_v = 0
def dfs(s, val = 1, cnt = 1):
    global max_v
    if s >= N:
        return
    val *= arr[s]
    if cnt == 2:
        max_v = max(val//10 + val%10, max_v)
        return
    for n in (s+1, N):
        dfs(n, val, cnt + 1)

for i in range(N):
    dfs(i)
print(max_v)
