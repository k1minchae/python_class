T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    x = 1
    for i in range(N):
        x *= (M-i)
    y = 1
    for j in range(1, N+1):
        y *= j
    print(int(x//y))