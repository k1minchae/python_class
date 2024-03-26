# 최단경로
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
V, E = map(int, input().split())
K = int(input()) # 시작노드
adj = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
result = [float('inf')] * (V+1)

pq = [(0, K)]
result[K] = 0
while pq:
    c, n = heappop(pq)
    if c > result[n]:
        continue
    for nc, nn in adj[n]:
        new_c = nc + c
        if new_c >= result[nn]:
            continue
        result[nn] = new_c
        heappush(pq, (new_c, nn))

for i in range(1, V+1):
    if result[i] == float('inf'):
        print('INF')
    else:
        print(result[i])
