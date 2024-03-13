# 12865 : 평범한 배낭
N, K = map(int, input().split())
DP = [0] * (K+1)
arr = [0] * 100001
for _ in range(N):
    W, V = map(int, input().split())
    if not arr[W] or arr[W] < V:
        arr[W] = V

