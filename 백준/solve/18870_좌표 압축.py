# # 좌표 압축
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# result = [0] * N    # 결과값을 저장할 리스트
#
# new_arr = []
# for i in range(N):
#     new_arr.append([arr[i], i]) # 값과 인덱스 저장
# new_arr.sort()
#
# idx = 0
# for i in range(0, N-1):
#     result[new_arr[i][1]] = idx
#     if new_arr[i][0] != new_arr[i+1][0]:
#         idx += 1
# result[new_arr[N-1][1]] = idx
#
# print(*result)
# import sys
# sys.stdin = open('input.txt', 'r')
result = 51  # result는 최대 50(N <= 50)


def dfs(s, limit, vt):
    global result
    if limit >= result:  # 백트래킹 (limit이 더 클경우 진행 x)
        return
    if s == sp:
        result = limit
        return
    cy, cx = s
    [[up, down]] = updown[cy][cx]
    # 현재 위치의 가로축을 탐색, 만약 가로축의 연속된 다른 좌표에 대하여 updown의 정보가 현재 위치와 똑같을 경우 vt에 추가(굳이 다시 돌아올 필요 x). 다를경우 그 좌표에서 위, 아래로 점프
    # vt에 추가 먼저
    for i in range(1, M):  # 왼쪽 탐색
        ny = cy
        nx = cx - i
        if [ny, nx] == sp:
            result = limit
            return
        if nx in range(M):
            if len(updown[ny][nx]) > 0 and updown[ny][nx][0] == [up, down]:
                vt.append([ny, nx])
            else:  # 반드시 연속된 좌표에 대하여 updown의 정보가 같을 경우에만 가지치기가 성립하기 때문에, 그외의 경우에는 break를 걸어준다
                break
    for i in range(1, M):  # 오른쪽 탐색
        ny = cy
        nx = cx + i
        if [ny, nx] == sp:
            result = limit
            return
        if nx in range(M):
            if len(updown[ny][nx]) > 0 and updown[ny][nx][0] == [up, down]:
                vt.append([ny, nx])

            else:
                break
    # 현재 좌표에선 위아래로 반드시 점프
    if updown[cy][cx][0][0] != -1 and [cy - updown[cy][cx][0][0], cx] not in vt:  # 현재 좌표에서 위로 점프 가능할경우
        dfs([cy - updown[cy][cx][0][0], cx], max(limit, updown[cy][cx][0][0]), vt + [[cy, cx]])
    if updown[cy][cx][0][1] != -1 and [cy + updown[cy][cx][0][1], cx] not in vt:  # 현재 좌표에서 아래로 점프 가능할경우
        dfs([cy + updown[cy][cx][0][1], cx], max(limit, updown[cy][cx][0][1]), vt + [[cy, cx]])
    for i in range(1, M):  # 가로축의 왼쪽으로 탐색
        ny = cy
        nx = cx - i
        if nx in range(M) and arr[ny][nx] == 0:  # 탐색중 바닥이 없을 경우 탐색 종료
            break
        if nx in range(M) and [ny, nx] not in vt:  # visited 한 곳이 아닐 경우 점프
            if updown[ny][nx][0][0] != -1:  # up 이 -1이 아닐 경우 위로 점프 가능, 점프 한 곳의 y 좌표는 ny - updown[ny][nx][0]
                dfs([ny - updown[ny][nx][0][0], nx], max(limit, updown[ny][nx][0][0]), vt + [[cy, cx]])
            if updown[ny][nx][0][1] != -1:  # 아래로 점프
                dfs([ny + updown[ny][nx][0][1], nx], max(limit, updown[ny][nx][0][1]), vt + [[cy, cx]])
    for i in range(1, M):  # 가로축의 오른쪽으로 탐색
        ny = cy
        nx = cx + i
        if nx in range(M) and arr[ny][nx] == 0:
            break
        if nx in range(M) and [ny, nx] not in vt:
            if updown[ny][nx][0][0] != -1:
                dfs([ny - updown[ny][nx][0][0], nx], max(limit, updown[ny][nx][0][0]), vt + [[cy, cx]])
            if updown[ny][nx][0][1] != -1:
                dfs([ny + updown[ny][nx][0][1], nx], max(limit, updown[ny][nx][0][1]), vt + [[cy, cx]])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directionup = []  # 위로 올라가는 direction
directiondown = []  # 내려가는 direction
updown = [[[] for _ in range(M)] for _ in range(N)]  # array의 좌표마다 올라갈 수 있는 가장 짧은 거리, 내려갈 수 있는 가장 짧은 거리를 저장하기 위한 list
for i in range(1, N):
    directionup.append(-i)
    directiondown.append(i)
for i in range(N):  # array에 대하여 각 발판에 대한 up down 정보 저장
    for j in range(M):  # up이나 down이 -1 일 경우 그쪽으로는 뛰지 못함
        if arr[i][j] == 2:
            sp = [i, j]
        if arr[i][j] == 3:
            goal = [i, j]
        if arr[i][j] != 0:
            for uy in directionup:
                ny = i + uy
                nx = j
                up = -1
                if ny < 0:
                    break
                elif arr[ny][nx] != 0:
                    up = -uy
                    break
            for dy in directiondown:
                ny = i + dy
                nx = j
                down = -1
                if ny >= N:
                    break
                elif arr[ny][nx] != 0:
                    down = dy
                    break
            updown[i][j].append([up, down])
dfs(goal, 0, [])  # goal에서부터 시작해서 sp까지 가기
