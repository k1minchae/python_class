# 발전소 설치
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, W = map(int, input().split()) # 노드 수, 간선 수
M = float(input()) # 제한 길이
power = [] # 발전소의 좌표를 저장할 리스트
linked = [[0] * N for _ in range(N)] # 이미 연결된 전선 표시하는 리스트

for _ in range(N):
    x, y = map(int, input().split())
    power.append((y, x))

# 이미 연결된 전선 표시
for _ in range(W):
    a, b = map(int, input().split())
    linked[a-1][b-1] = 1
    linked[b-1][a-1] = 1

def dijkstra():
    pq = [(0, 0, power[0][0], power[0][1])] # 비용, 발전소 번호, y좌표, x좌표
    visited = [float('inf')] * N
    visited[0] = 1

    while pq:
        cost, node, y, x = heappop(pq)
        if cost > visited[node]:
            continue
        # 발전소 리스트 순회해서 다음 좌표 탐색할거임
        for next_node in range(N):
            if next_node == node: # 자기자신은 탐색하지 않음
                continue
            # ny, nx 은 다음 발전소의 좌표
            ny = power[next_node][0]
            nx = power[next_node][1]
            if linked[node][next_node]: # 만약 이미 연결된 전선이라면 거리 = 0으로 처리
                dis = 0
            else: # 연결되지 않은 전선이라면 거리 계산
                dis = ((ny-y) ** 2 + (nx-x) ** 2) ** 0.5
            if dis > M: # 거리가 제한길이 초과라면 pass
                continue
            new_cost = dis + cost # 비용 갱신
            if new_cost < visited[next_node]:
                visited[next_node] = new_cost
                heappush(pq, (new_cost, next_node, ny, nx))
    return int(visited[N-1] * 1000)

print(dijkstra())