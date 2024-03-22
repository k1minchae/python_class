# 최소 스패닝 트리
import sys
input = sys.stdin.readline
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
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

V, E = map(int, input().split())
parents = [i for i in range(V)]
adj = []
for _ in range(E):
    a, b, c = map(int, input().split())
    adj.append((a-1, b-1, c))
adj.sort(key=lambda x : x[2])

cnt = 0
total = 0
for a, b, c in adj:
    if find(a) != find(b):
        cnt += 1
        union(a, b)
        total += c
        if cnt == V-1:
            break
print(total)
