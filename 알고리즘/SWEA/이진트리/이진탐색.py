# 이진 탐색
def f(s):
    global node
    if s > N:
        return
    f(s * 2)
    tree[s] = node
    node += 1
    f(s * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    node = 1
    f(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')