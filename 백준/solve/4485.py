import sys
from heapq import heappop, heappush
input = sys.stdin.readline
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dijkstra():
    q = [(arr[0][0], 0, 0)] # 시작점의 도둑루피, y좌표, x좌표
    result = [[float('inf')] * N for _ in range(N)]
    result[0][0] = arr[0][0] # 시작 좌표에 도둑루피값 입력하고 시작

    while q:
        cost, y, x = heappop(q) # 도둑루피, y좌표, x좌표
        if cost > result[y][x]: # heap특성상 큰 값이 나중에 남아있으므로 걸러냄
            continue
        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N: # 범위 안에서
                next_cost = cost + arr[ny][nx] # 다음 이동시 도둑루피 합계 구하기
                if next_cost >= result[ny][nx]: # 전에 이동했던 값과 비교해서 더 크면 거르기
                    continue
                heappush(q, (next_cost, ny, nx)) # heap 에 저장
                result[ny][nx] = next_cost # 결과에도 저장
    return result[N-1][N-1]

tc = 1
while True:
    N = int(input()) # 동굴의 크기
    if N == 0:
        exit()
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {tc}:', dijkstra())
    tc += 1
