# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sy = 0
sx = 0

# 아기상어의 초기 위치 구하는 함수
def find_baby():
    global sy, sx
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                sy = i
                sx = j
                return

dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]    # 위, 왼, 오, 아래
# 먹을 수 있는 물고기를 찾는 함수
def find_fish(sy, sx, size_ = 2):
    arr[sy][sx] = 0
    visited = [[-1] * N for _ in range(N)]
    q = deque([(sy, sx)])
    visited[sy][sx] = 0  # 거리 기록함
    size = size_

    fishes = []
    while q:
        y, x = q.popleft()
        # 물고기에 도달했을 경우
        if 1 <= arr[y][x] < 7 and arr[y][x] < size:
            fishes.append((visited[y][x], y, x))

        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] <= size and visited[ny][nx] == -1:
                visited[ny][nx] = 1 + visited[y][x]
                q.append((ny, nx))
    if fishes:
        fishes.sort(key=lambda x:(x[0], x[1], x[2]))
    return fishes   # 현 위치에서 먹을 수 있는 물고기들 반환

# 물고기를 먹으러 가는 함수
def go_eat(sy, sx, size_ = 2, eat_ = 0):
    size = size_
    eat = eat_
    eatable = find_fish(sy, sx, size)
    if not eatable:
        return 0

    tar_y = eatable[0][1]
    tar_x = eatable[0][2]

    q = deque([(sy, sx)])
    times = [[-1] * N for _ in range(N)]  # 시간을 기록함
    times[sy][sx] = 0

    while q:
        y, x = q.popleft()
        if y == tar_y and x == tar_x:
            arr[tar_y][tar_x] = 0
            eat += 1
            if eat == size:
                size += 1
                eat = 0
            result = times[y][x] + go_eat(y, x, size, eat)
            return result
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] <= size and times[ny][nx] == -1:
                q.append((ny, nx))
                times[ny][nx] = times[y][x] + 1

find_baby() # 초기위치 찾고
print(go_eat(sy, sx))
