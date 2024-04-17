#  도미노
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
T = int(input())
def dfs(x, lst):
    for nx in lst[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx, lst)
    stack.append(x)

for _ in range(T):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)] # 인접리스트
    r_adj = [[] for _ in range(N)] # reversed adj
    scc = [] # 사이클 발생하는부분의 부모노드 저장할 배열

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        r_adj[b-1].append(a-1)

    stack = []
    visited = [0] * N
    for i in range(N):
        if not visited[i]:
            dfs(i, adj)

    visited = [0] * N
    while stack:
        x = stack.pop()
        if not visited[x]:
            visited[x] = 1
            dfs(x, r_adj)
            scc.append(x)
    visited = [0] * N
    ans = 0
    for x in scc:
        if not visited[x]:
            visited[x] = 1
            ans += 1
            dfs(x, adj)
    print(ans)
