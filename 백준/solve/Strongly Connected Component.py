# Strongly Connected Component
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs_first(v):
    visited[v] = True
    for nxt in adj[v]:
        if not visited[nxt]:
            dfs_first(nxt)
    stack.append(v)

def dfs_second(v, scc_num):
    visited[v] = True
    component[scc_num].append(v+1)  # 원래 인덱스는 1부터라서 + 1해줌
    for nxt in r_adj[v]:
        if not visited[nxt]:
            dfs_second(nxt, scc_num)


V, E = map(int, input().split())
adj = [[] for _ in range(V)]
r_adj = [[] for _ in range(V)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    r_adj[b-1].append(a-1)

visited = [False] * V
stack = []

# 정방향 그래프에서 DFS 수행
for i in range(V):
    if not visited[i]:
        dfs_first(i)

visited = [False] * V
component = []
scc_num = 0

# 역방향 그래프에서 DFS 수행
while stack:
    v = stack.pop()
    if not visited[v]:
        component.append([])
        dfs_second(v, scc_num)
        scc_num += 1

# 출력 형식에 맞게 결과 정렬
component = [sorted(list) for list in component]
component.sort()

print(len(component))
for comp in component:
    print(*comp, -1)