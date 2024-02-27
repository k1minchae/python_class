# 최소합
# 내 코드
# T = int(input())
#
# def min_sum(y, x, val=0):
#     global min_val
#     if y < 0 or x < 0 or y >= N or x >= N:
#         return
#     if val > min_val:
#         return
#     if y == x == N-1:
#         min_val = min(val+arr[y][x], min_val)
#         return
#     min_sum(y+1, x, val + arr[y][x])
#     min_sum(y, x+1, val + arr[y][x])
#
# for tc in range(1, T+1):
#     min_val = float('inf')
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     min_sum(0, 0)
#     print(f'#{tc} {min_val}')



# 강사님 코드
# dir = [(0, 1), (1, 0)]
#
# def dfs(x, y, sum_v):
#     global result
#     if sum_v >= result: # 가지치기
#         return
#     if x == N - 1 and y == N -1: # 목표 지점에 도착
#         if sum_v < result:
#             result = sum_v
#         return
#
#     for dx, dy in dir:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             dfs(nx, ny, sum_v + arr[ny][ny])
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     result = float('inf')
#     dfs(0, 0, arr[0][0])    # 첫 번째 좌표부터 누적합
#     print(f'#{tc} {result}')