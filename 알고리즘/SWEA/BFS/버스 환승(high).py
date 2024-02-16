# 버스 환승(high)
from collections import deque
def crs(bus1, bus2):
    [sx1, sy1, dx1, dy1] = bus1
    [sx2, sy2, dx2, dy2] = bus2
    if min(sx1, dx1) < max(sx2, dx2) and min(sy1, dy1) < max(sy2, dy2):
        return True
    else:
        return False

def BFS()
    if SX ==

m, n = map(int, input().split())
k = int(input())  # 버스 수
arr = []
for i in range(k):
    arr.append(list(map(int, input().split()))[1:]) # 버스
SX, SY, DX, DY = map(int, input().split())  # 내가 출발할 곳, 도착할 곳

print(arr)
arr += [[SX, SY, SX, SY],[DX,DY,DX,DY]]