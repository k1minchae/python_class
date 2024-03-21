from heapq import heappop, heappush

V, E = map(int, input().split())
start = 0 # 시작 노드 번호

# 인접 리스트
graph = [[] for _ in range(V)]

# 누적 거리를 저장할 변수
distance = [float('inf')] * V # 엄청 큰 값으로 초기화

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

def dijkstra(start):
    pq = [] # 우선순위 큐

    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0 # 이거 안 하면 다시 여기로 돌아와서 싸이클 발생

    while pq:
        # 최단거리 노드에 대한 정보
        dist, now = heappop(pq)

        # now 가 이미 더 짧은 거리로 온 적이 있다면 pass
        # pq 의 특성때문에 더 긴 거리도 저장되어있기 때문에 처리 해줘야함
        if distance[now] < dist:
            continue

        # now 에서 갈 수 있는 인접 노드 확인
        for next_dist, next_node in graph[now]:
            new_dist = dist + next_dist # 누적 거리 계산 (여태온 거리 + 다음에 올 거리)

            # 이미 더 짧은 거리가 있는 경우는 pass
            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist  # 최단 거리일경우 누적거리 갱신
            heappush(pq, (new_dist, next_node)) # next_node 의 인접노드들을 pq에 추가

dijkstra(0)
print(distance)
