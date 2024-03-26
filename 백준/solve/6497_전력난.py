# 전력난
import sys
input = sys.stdin.readline
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
    parents[y] = x

while True:
    m, n = map(int, input().split()) # 노드, 간선
    if m == n == 0:
        break
    arr = []
    max_d = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        arr.append((z, x, y))
        max_d += z
    arr.sort()
    parents = [i for i in range(m+1)]
    dis = 0
    cnt = 0
    for d, a, b in arr:
        if find(a) != find(b):
            cnt += 1
            dis += d
            union(a, b)
        if cnt == m - 1:
            break
    print(max_d - dis)
