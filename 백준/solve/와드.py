# 와드
import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
sy, sx = map(int, input().split())
trip = list(input().rstrip())
dir = {'U': (-1, 0),
       'D': (1, 0),
       'L': (0, -1),
       'R': (0, 1)
}
result = [['#'] * M for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def wad(sy, sx):
    q = deque([(sy, sx)])
    space = arr[sy][sx]
    result[sy][sx] = '.'
    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and result[ny][nx] == '#' and space == arr[ny][nx]:
                q.append((ny, nx))
                result[ny][nx] = '.'
y = sy - 1
x = sx - 1
for t in trip:
    if t == 'W':
        if result[y][x] == '#':
            wad(y, x)
    else:
        dy, dx = dir[t]
        y += dy
        x += dx
result[y][x] = '.'
for dy, dx in directions:
    ny = y + dy
    nx = x + dx
    if 0 <= ny < N and 0 <= nx < M:
        result[ny][nx] = '.'

for r in result:
    print(*r, sep='')
