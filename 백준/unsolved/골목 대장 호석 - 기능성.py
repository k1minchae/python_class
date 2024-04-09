# 골목 대장 호석 - 기능성
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M, S, E, C = map(int, input().split())
adj = [[]for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))
min_h = float('inf')
visited = [0] * (N+1)
def dfs(n=S, h=0, c=0): # 노드번호, 수치심, 남은돈
    global min_h
    visited[n] = 1
    if n == E:
        min_h = min(h, min_h)
        return
    for nc, nn in adj[n]:
        if not visited[nn] and nc+c <= C:
            visited[nn] = 1
            dfs(nn, max(h, nc), c+nc)
            visited[nn] = 0
dfs()
if min_h == float('inf'):
    print(-1)
else:
    print(min_h)