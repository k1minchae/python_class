# 민준이와 마산 그리고 건우
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
N, M, tar = map(int, input().split())
tar -= 1
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a-1].append((c, b-1))
    adj[b-1].append((c, a-1))

def dijkstra(start, end):
    q = [(0, start)]
    visited = [float('inf')] * N
    visited[start] = 0
    while q:
        c, x = heappop(q)
        if visited[x] < c:
            continue
        for nc, nx in adj[x]:
            next_cost = nc + c
            if visited[nx] <= next_cost:
                continue
            visited[nx] = next_cost
            heappush(q, (next_cost, nx))
    return visited[end]

# 도착점까지의 최단경로
direct = dijkstra(0, N-1)

# 민준이 들려서 도착점가는 거리
to_minjun = dijkstra(0, tar) + dijkstra(tar, N-1)

if direct == to_minjun: # 민준이 들리는거와 최단경로가 같다면
    print('SAVE HIM')
else:
    print('GOOD BYE')