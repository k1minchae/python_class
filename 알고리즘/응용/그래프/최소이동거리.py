# 5251 최소이동거리
from heapq import heappush, heappop
def dijkstra(start=0):
    pq = [(0, start)]   # 비용, node
    costs[0] = 0
    while pq:
        cost, node = heappop(pq)
        if cost > costs[node]:
            continue

        for next_cost, next_node in adj[node]:
            new_cost = next_cost + cost

            if new_cost >= costs[next_node]:
                continue
            costs[next_node] = new_cost
            heappush(pq, (new_cost, next_node))

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())   # 노드: 0~N , 도로개수 E
    adj = [[] for _ in range(N+1)]

    costs = [10**6] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))

    dijkstra()
    print(f'#{tc}', costs[-1])