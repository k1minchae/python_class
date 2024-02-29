def find(y, x):
    # 가로
    cnt_h = 0
    for j in range(N):
        if arr[y][j] == 'o':
            cnt_h += 1
        else:
            cnt_h = 0
        if cnt_h == 5:
            return True

    # 세로
    cnt_v = 0
    for i in range(N):
        if arr[i][x] == 'o':
            cnt_v += 1
        else:
            cnt_v = 0
        if cnt_v == 5:
            return True

    # 대각 (우하향)
    cnt_c = 0
    for k in range(-4, 5):
        if 0 <= y + k < N and 0 <= x + k < N:
            if arr[y+k][x+k] == 'o':
                cnt_c += 1
            else:
                cnt_c = 0
            if cnt_c == 5:
                return True

    # 대각 (우상향)
    cnt_c = 0
    for k in range(-4, 5):
        if 0 <= y - k < N and 0 <= x + k < N:
            if arr[y - k][x + k] == 'o':
                cnt_c += 1
            else:
                cnt_c = 0
            if cnt_c == 5:
                return True

def final():
    for Y in range(N):
        for X in range(N):
            check = find(Y, X)
            if check:
                return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = final()
    print(f'#{tc} {result}')


# 강사님 코드
def omok(y, x):
    dy = [1, 0, 1, -1]  # 아래, 오른쪽 우하향, 우상향
    dx = [0, 1, 1, 1]

    # 네 방향 탐색
    for dir in range(4):
        cnt = 1 # 기준 좌표에 돌이 있으므로 1부터 시작
        # 돌 4개 탐색
        for k in range(1, 5):
            ny = y + (dy[dir] * k)
            nx = x + (dx[dir] * k)
            if not (0 <= ny < N and 0 <= nx < N): break

            # 돌을 발견하면 count
            if arr[ny][nx] == 'o': cnt += 1

            if cnt == 5:
                return True
    return False

def game_start():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                if omok(r, c):
                    return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = final()
    print(f'#{tc} {result}')
