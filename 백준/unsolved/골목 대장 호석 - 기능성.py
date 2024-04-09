# 골목 대장 호석 - 기능성
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M, S, E, C = map(int, input().split())
adj = [[]for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((-c, b))
    adj[b].append((-c, a))

def dijkstra():
    q = [(0, S)]
    result = [float('-inf')] * (N+1)
    result[S] = 0
    max_h = 0
    while q:
        c, x = heappop(q)
        if c < result[x]:
            continue
        for cost, nx in adj[x]:
            nc = c + cost
            if nc < -C or result[nx] > nc:
                continue
            max_h = max(max_h, -cost)
            result[nx] = nc
            heappush(q, (nc, nx))
    if result[E] == float('-inf'):
        return -1
    return -result[E]
print(dijkstra())
