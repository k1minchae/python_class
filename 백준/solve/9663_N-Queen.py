# # N-Queen
# dy = [-1, 1, 0, 0, -1, -1, 1, 1]
# dx = [0, 0, 1, -1, -1, 1, -1, 1]
#
# def mark_visited(y, x, visited, mark):
#     for d in range(8):  # 상하좌우 대각선
#         for k in range(1, N):   # 퀸의 공격범위
#             ny = y + dy[d] * k
#             nx = x + dx[d] * k
#             if 0 <= ny < N and 0 <= nx < N:
#                 visited[ny][nx] += mark
#
# def queen(y, visited):
#     global cnt
#     if y == N:  # 퀸 전부다 놓았다면
#         cnt += 1
#         return
#     # x 좌표 순회
#     for x in range(N):
#         # 놓을 수 있다면
#         if not visited[y][x]:
#             visited[y][x] = 1   # 놓기
#             mark_visited(y, x, visited, 1)  # 공격 범위 방문처리
#             queen(y+1, visited)  # 다음 y 좌표로 이동
#
#             # 백트래킹
#             visited[y][x] = 0   # 되돌리기
#             mark_visited(y, x, visited, -1)  # 공격 범위도 되돌리기
#
#
# N = int(input())
#
# visited = [[0] * N for _ in range(N)]
# cnt = 0
# queen(0, visited)
# print(cnt)

dy = [-1, 1, 0, 0]  # 상하좌우
dx = [0, 0, 1, -1]

def queen(y):
    global cnt
    if y == N:
        cnt += 1
        return
    for x in range(N):
        # 열, 대각선에 다 없으면
        if not col_check[x] and not diag1_check[y + x] and not diag2_check[y - x + N - 1]:
            col_check[x] = diag1_check[y + x] = diag2_check[y - x + N - 1] = 1  # 방문처리
            queen(y + 1)    # 다음 행으로 이동
            col_check[x] = diag1_check[y + x] = diag2_check[y - x + N - 1] = 0  # 방문처리 되돌리기

N = int(input())

# 열 확인리스트와 대각선 리스트
col_check = [0] * N
diag1_check = [0] * (2 * N - 1) # 우상향
diag2_check = [0] * (2 * N - 1) # 좌상향

cnt = 0
queen(0)
print(cnt)