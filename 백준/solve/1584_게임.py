# 게임
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
def dijkstra(sy=0, sx=0):
    pq = [(0, sy, sx)]
    result[sy][sx] = 0

    while pq:
        cost, y, x = heappop(pq)
        if result[y][x] < cost:
            return
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < 501 and 0 <= nx < 501 and arr[ny][nx] != 2:
                if arr[ny][nx] == 1: new_cost = cost + 1
                else:   new_cost = cost
                if result[ny][nx] > new_cost:
                    result[ny][nx] = new_cost
                    heappush(pq, (new_cost, ny, nx))
    if result[500][500] == float('inf'):
        return -1
    return result[500][500]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input()) # 위험한 구역의 수
arr = [[0] * 501 for _ in range(501)]
for _ in range(N): # 위험한 구역의 좌표
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(y1, y2+1):
        for j in range(x1, x2 + 1):
            arr[i][j] = 1
M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            arr[i][j] = 2
result = [[float('inf')] * 501 for _ in range(501)]
print(dijkstra())