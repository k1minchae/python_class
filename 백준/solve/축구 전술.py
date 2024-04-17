# 축구 전술
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
T = int(input())
def dfs(x, adj_lst):
    for nx in adj_lst[x]:
        if visited[nx] == -1:
            visited[nx] = visited[x]
            dfs(nx, adj_lst)
    stack.append(x)
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    r_adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        r_adj[b].append(a)
    stack = []
    scc = []
    visited = [-1] * N
    for i in range(N):
        if visited[i] == -1:
            visited[i] = i
            dfs(i, adj)

    visited = [-1] * N
    while stack:
        i = stack.pop()
        if visited[i] == -1:
            visited[i] = i
            dfs(i, r_adj)
            scc.append(i)

    result = []
    for i in range(N):
        # 첫번째 위상과 연결된것들을 result에 추가
        if visited[i] == scc[0]:
            result.append(i)

    visited = [-1] * N
    visited[scc[0]] = scc[0]
    dfs(scc[0], adj)
    for i in range(N):
        # 만약 첫번째 싸이클 돌려도 방문못하는곳 있으면 confused
        if visited[i] == -1:
            print('Confused')
            print()
            break
    # 방문가능하면 첫번째 사이클이 모두 정답이 될수 있으므로 result배열 출력
    else:
        for i in result:
            print(i)
        print()
    if tc != T:
        input()
