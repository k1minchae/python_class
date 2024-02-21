T = int(input())
def f(s):
    if s <= N:
        if not tree[s]:
            tree[s] = f(s*2) + f(s*2+1)
        if tree[s]:
            return tree[s]
    else:
        return 0
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        l_node, num = map(int, input().split())
        tree[l_node] = num
    print(f'#{tc} {f(L)}')