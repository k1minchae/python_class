# 빙산
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 인접한 곳 다 지워주는 DFS 함수
def dfs(sy, sx, lst):
    lst[sy][sx] = 0 # 좌표를 지워줌
    for dy, dx in dir:
        ny = sy + dy
        nx = sx + dx
        # 인접한 곳이 있다면
        if 0 < ny < N and 0 < nx < M and lst[ny][nx]:
            dfs(ny, nx, lst) # 거기도 가서 지워줌

ice = []
for i in range(1, N):
    for j in range(1, M):
        if arr[i][j]:
            ice.append((i, j, arr[i][j]))

ice = deque(ice)
year = 0
while ice:
    ice_cnt = 0
    # DFS 로 인접한 빙산을 지울거기 때문에 원본 리스트를 복사해서 사용
    lst = [i[:] for i in arr]
    for i in range(1, N):
        for j in range(1, M):
            if lst[i][j]: # 빙산 발견하면
                ice_cnt += 1 # 빙산 덩어리 개수 cnt
                dfs(i, j, lst)  # DFS 로 발견한 빙산과 인접한 빙산 다 지우기
    if ice_cnt > 1: # 2덩어리 이상이 됐다면 break 걸고 year 출력
        break

    year += 1 # 아직 2덩어리가 안됐으니 1년더 녹여보기
    melt = [] # 녹은 얼음을 저장하는 리스트

    # 년도가 바뀔 때 얼음을 순회하며 녹인다
    for i in range(len(ice)):
        y, x, ice_size = ice.popleft()  # 좌표 + 얼음의 양
        zero = 0 # 주변에 0 이 얼마나 있는지 세주는 변수
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if not arr[ny][nx]: # 0이 있다면 세준다
                zero += 1

        # 주변에 0 이 있는 만큼 얼음의 양 줄여주기
        ice_size -= zero
        if ice_size > 0:    # 얼음이 남아 있다면
            ice.append((y, x, ice_size))    # 다시 큐에 추가
        else:   # 얼음이 다 녹았다면 큐에 추가 안하고
            melt.append((y, x)) # 녹은 얼음 리스트에 추가

    # 순회 중간에 녹여주면 뒷 얼음에 영향을 미칠 수 있으므로
    # 얼음 확인하는 순회가 끝났을 때 한번에 녹여준다
    for y, x in melt: # 녹은 얼음 리스트를 순회해서
        arr[y][x] = 0 # 해당 좌표를 전부 0 으로 만들어줌

else:   # 얼음 다 녹았는데도 break 안됐다면 (while-else 사용)
    year = 0    # 0 출력

print(year)