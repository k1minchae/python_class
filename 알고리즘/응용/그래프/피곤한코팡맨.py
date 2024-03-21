# 피곤한 코팡맨
from heapq import heappop, heappush

def dijkstra(sy, sx):
    pq = [(0, sy, sx)]
    tired[sy][sx] = 0

    while pq:
        w, y, x = heappop(pq)
        if w > tired[y][x]:
            continue
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N:
                h = abs(h_arr[y][x] - h_arr[ny][nx])
                new_w = h
                if new_w < tired[ny][nx]:
                    heappush(pq, (new_w, ny, nx))
                    tired[ny][nx] = new_w

N = int(input())
arr = [list(input()) for _ in range(N)]
h_arr = [list(map(int, input().split())) for _ in range(N)]
tired = [[float('inf')] * N for _ in range(N)]
post_y = 0
post_x = 0
houses = []
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'P':
            post_x = j
            post_y = i
            break
        if arr[i][j] == 'K':
            houses.append((i, j))

dijkstra(post_y, post_x)
result = []
for hy, hx in houses:
    result.append(tired[hy][hx])
print(sum(result) + min(result))
print(result)
print(tired)