# 부분 수열의 합
def dfs(x, sum_v=0):
    global cnt
    sum_v += arr[x]
    if sum_v == K:
        cnt += 1
    if sum_v > K:
        return
    for nx in range(x+1, N):
        dfs(nx, sum_v)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        dfs(i)
    print(f'#{tc}', cnt)