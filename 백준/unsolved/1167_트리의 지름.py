# 트리의 지름
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

def dfs(v, dis=0):
    global max_d
    max_d = max(dis, max_d)
    for w in range(0, len(adj[v]), 2):
        next = adj[v][w]
        cost = adj[v][w+1]
        if visited[next]:
            continue
        visited[next] = 1
        dfs(next, dis+cost)
        visited[next] = 0

N = int(input())
parents = [i for i in range(N+1)]
adj = [[] for _ in range(N+1)]
for _ in range(N):
    v, *lst, dump = map(int, input().split())
    for i in range(0, len(lst), 2):
        union(v, lst[i])
        adj[v] += lst

for i in range(1, N+1):
    find(i)
max_d = 0
for i in set(parents):
    if not i:
        continue
    visited = [0] * (N+1)
    visited[i] = 1
    dfs(i)
print(max_d)
