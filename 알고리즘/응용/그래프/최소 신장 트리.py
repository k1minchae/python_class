# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    # 서로소를 구하는게 아니라서 rank 필요 X
    parents[y] = x


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    parents = [i for i in range(V+1)]

    arr = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr.append((s, e, w))
    arr.sort(key=lambda x: x[2])

    level = 0  # 선택한 수
    total = 0
    # 모든 간선을 확인한다
    for s, e, w in arr:
        # 이미 같은 집합에 속해있다면 pass
        if find(s) == find(e):
            continue
        union(s, e)
        level += 1
        total += w
        if level == V:
            break
    print(f'#{tc} {total}')