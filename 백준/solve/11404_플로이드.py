import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = [[float('inf')]*N for _ in range(N)]
# 자신 -> 자신은 0
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    a, b, c, = map(int, input().split())
    # a->b 에 대해서 더 적은 요금이 들어올수도 있으므로 최소값으로 갱신
    arr[a-1][b-1] = min(c, arr[a-1][b-1])

for k in range(N): # 경유지
    for i in range(N):
        for j in range(N):
            # i -> j 로 갈때 k를 경유해서 가는것과 직통으로 가는것 비교
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(N):
    for j in range(N):
        if arr[i][j] == float('inf'):
            arr[i][j] = 0
        print(arr[i][j], end=' ')
    print()