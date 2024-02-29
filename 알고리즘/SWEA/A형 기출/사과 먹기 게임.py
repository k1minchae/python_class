# 사과 먹기 게임
from collections import deque

dy = [0, 1, 0, -1]  # turn 값이 증가할때마다 오른쪽으로 회전
dx = [1, 0, -1, 0]


def apple(sy, sx, turn, cnt, m):
    q = deque([[sy, sx, turn, cnt, m]])  # 시작 좌표, turn 횟수, 연속으로 회전한 수, 찾을 사과 번호
    while q:
        y, x, turn, cnt, m = q.popleft()
        if m > last_apple:  # 모든 사과 탐색 완료
            return
        if arr[y][x] == m:  # 사과 찾으면
            M[m][2] = min(turn, M[m][2])
            m += 1  # 다음 사과로

        ny = y + dy[turn % 4]
        nx = x + dx[turn % 4]
        if 0 <= ny < N and 0 <= nx < N:  # 범위 설정
            # 가지치기 (한바퀴 회전한 경우와 사과에 저장된 회전값보다 큰 경우 제외)
            if cnt < 4 and turn < M[m][2]:
                q.append([ny, nx, turn, 0, m])
                q.append([ny, nx, turn + 1, cnt + 1, m])


T = int(input())
for tc in range(1, T + 1):
    result = 10 ** 6
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M = [[0, 0, 0] for _ in range(12)]  # 인덱스 에러 방지로 1개 더
    last_apple = 0  # 마지막 사과 번호 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                last_apple = max(arr[i][j], last_apple)
                M[arr[i][j]] = [i, j, 10 ** 6]  # 사과의 y, x, turn 횟수

    if M[1][0] > 0:  # 첫 사과가 첫번째줄에 있는 경우 (turn = 0)
        apple(M[1][0], M[1][1], 1, 1, 1)  # y좌표, x좌표, turn = 1, 연속회전수 = 1, 찾을 사과 =1
    else:  # 두번째 줄 이상에 있는 경우 (turn = 1)
        apple(M[1][0], M[1][1], 0, 0, 1)
    print(f'#{tc} {M[last_apple][2]}')