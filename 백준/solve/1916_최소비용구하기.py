# 최소비용구하기
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = int(input()), int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
S, E = map(int, input().split())
result = [float('inf')] * (N + 1)
def dijkstra(s):
    pq = [(0, s)]
    result[s] = 0
    while pq:
        cost, node = heappop(pq)
        if result[node] < cost:
            continue
        for next_cost, next_node in adj[node]:
            sum_cost = next_cost + cost
            if sum_cost >= result[next_node]:
                continue
            heappush(pq, (sum_cost, next_node))
            result[next_node] = sum_cost
    return result[E]
print(dijkstra(S))
