# 경찰서
import sys
input = sys.stdin.readline
def dfs(x):
    for nx in adj[x]:
        if visited[nx] == 0:
            visited[nx] = 1
            dfs(nx)
    stack.append(x)

def dfs_reverse(x, idx):
    scc[idx].append(x)
    for nx in r_adj[x]:
        if visited[nx] == 0:
            visited[nx] = 1
            dfs_reverse(nx, idx)

N = int(input())
costs = list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(N)]
adj = [[] for _ in range(N)]
r_adj = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            adj[i].append(j)
            r_adj[j].append(i)

visited = [0] * N
stack = []
for i in range(N):
    if not visited[i]:
        visited[i] = 1
        dfs(i)

scc_idx = 0
visited = [0] * N
scc = []
while stack:
    x = stack.pop()
    if not visited[x]:
        scc.append([])
        visited[x] = 1
        dfs_reverse(x, scc_idx)
        scc_idx += 1

cost = 0
for i in scc:
    min_c = float('inf')
    for node in i:
        min_c = min(costs[node], min_c)
    cost += min_c

print(cost)