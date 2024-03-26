# 네트워크 연결
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
    parents[y] = x
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
parents = [i for i in range(N+1)]
cost = 0
cnt = 0
arr = []
for _ in range(M):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))
arr.sort()
for c, a, b, in arr:
    if cnt == M:
        break
    if find(a) != find(b):
        cost += c
        union(a, b)
        cnt += 1

print(cost)