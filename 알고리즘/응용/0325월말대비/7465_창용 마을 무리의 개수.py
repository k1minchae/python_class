# 창용 마을 무리의 개수
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        parents[y] = x
    elif rank[y] > rank[x]:
        parents[x] = y
    else:
        rank[x] += 1
        parents[y] = x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 사람수, 관계수
    parents = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    for i in range(N+1):
        find(i)
    print(f'#{tc}', len(set(parents)) - 1)

