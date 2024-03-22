# 장훈이의 높은 선반
def DFS(x, sum_v = 0):
    global min_sum
    sum_v += arr[x]
    if sum_v >= B:
        min_sum = min(min_sum, sum_v)
        return
    for nx in range(x+1, N):
        DFS(nx, sum_v)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # 사람수 : N, B: 높이
    arr = list(map(int, input().split()))
    min_sum = 10 ** 6
    visited = [0] * N
    for i in range(N):
        DFS(i)
    print(f'#{tc} {min_sum-B}')