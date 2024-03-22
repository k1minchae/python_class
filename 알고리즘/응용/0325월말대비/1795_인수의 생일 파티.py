# 인수의 생일 파티
from heapq import heappop, heappush

def dijkstra(s, result, adj):
    pq = [(s, 0)]
    result[s] = 0
    while pq:
        node, cost = heappop(pq)
        if cost > result[node]:
            continue
        for next_node, next_cost in adj[node]:
            next_cost = next_cost + cost
            if next_cost < result[next_node]:
                heappush(pq, (next_node, next_cost))
                result[next_node] = next_cost

T = int(input())
for tc in range(1, T+1):
    N, M, S = map(int, input().split()) # 노드수, 간선수, 시작노드
    come = [[] for _ in range(N + 1)]
    go = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        come[a].append((b, c))
        go[b].append((a, c))
    result_come = [float('inf')] * (N+1)
    result_go = [float('inf')] * (N + 1)

    dijkstra(S, result_come, come)
    dijkstra(S, result_go, go)
    max_v = 0
    for i in range(1, N+1):
        val = result_go[i] + result_come[i]
        if val > max_v:
            max_v = val
    print(f'#{tc}', max_v)