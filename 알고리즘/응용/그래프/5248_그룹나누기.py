def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[x] = y
    else:
        parents[y] = x
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    parents = [i for i in range(N+1)]

    for i in range(0, M * 2, 2):
        x = arr[i]
        y = arr[i+1]
        union(x, y)

    # 아직 조상값으로 갱신되지 않은 정점을 갱신해줌
    for i in range(N+1):
        find_set(i)

    print(parents)