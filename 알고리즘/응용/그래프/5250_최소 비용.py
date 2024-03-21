# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용
from heapq import heappop, heappush
def dijkstra(sy=0, sx=0):
    pq = [(0, sy, sx)] # 가중치, 좌표
    distance[0][0] = 0

    while pq:
        w, y, x = heappop(pq)
        # 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[y][x] < w:
            continue
        # 다음 좌표 살펴보기
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] - arr[y][x] > 0: # 더높은곳이라면
                    h = arr[ny][nx] - arr[y][x] # 높이차 구하기
                else: h = 0 # 더 높지 않다면 높이차 0

                new_w = h + w + 1 # 누적 가중치 : 높이차 + 기존가중치 + 1
                if new_w >= distance[ny][nx]:
                    continue
                distance[ny][nx] = new_w
                heappush(pq, (new_w, ny, nx))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[10**6] * N for _ in range(N)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dijkstra()
    print(f'#{tc}', distance[N-1][N-1])
