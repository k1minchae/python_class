# 재미있는 오셀로 게임
dy = [-1, 1, 0, 0, -1, -1, 1, 1]    # 8 방향 탐색
dx = [0, 0, -1, 1, -1, 1, -1, 1]

def game(y, x):
    stone = arr[y][x]
    for d in range(8):
        temp = [] # 뒤집을 돌의 임시리스트
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= N or nx >= N or arr[ny][nx] == 0: # 돌 못발견 or 범위밖
            continue

        elif arr[ny][nx] != stone: # 적팀 돌 발견
            temp.append([ny, nx]) # 뒤집을 돌 리스트에 추가

            while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != stone and arr[ny][nx] != 0: # 범위 안에서 계속 적팀 돌을 만나면
                ny += dy[d] # 한 칸 더 이동하기
                nx += dx[d]
                if 0 <= ny < N and 0 <= nx < N: # 한칸 더 갔을 때 범위 안이라면
                    if arr[ny][nx] != stone and arr[ny][nx] != 0:   # 또 적팀 돌이라면
                        temp.append([ny, nx]) # 뒤집을 돌 추가

                    if arr[ny][nx] == stone:  # 다시 내 돌을 만나면
                        for i, j in temp:
                            arr[i][j] = reverse_stone(i, j) # 리스트에 있는 돌들 전부 뒤집기
                        temp.clear() # 다 뒤집었다면 clear

            if temp:    # 뒤집지 못했다면 clear
                temp.clear()

def reverse_stone(y, x):
    stone = arr[y][x]
    if stone == 2:
        return 1
    if stone == 1:
        return 2

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 초기 리스트
    arr = [[0] * N for _ in range(N)]
    arr[(N-1)//2][(N-1)//2] = 2
    arr[(N-1)//2][(N-1)//2+1] = 1
    arr[(N-1)//2+1][(N-1)//2] = 1
    arr[(N-1)//2+1][(N-1)//2+1] = 2

    for _ in range(M):
        # x, y, 돌종류
        a, b, s = map(int, input().split())
        arr[b-1][a-1] = s
        # 돌 추가할때마다 game 돌리기
        game(b-1, a-1)

    # 게임 다 끝났으면 돌 세기
    w_cnt = 0
    b_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                b_cnt += 1
            elif arr[i][j] == 2:
                w_cnt += 1
    print(f'#{tc} {b_cnt} {w_cnt}')


B = 1
W = 2
dir = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

# 뒤집을 돌의 좌표를 구해주는 함수
def get_reverse_stone(y, x, bang, color):
    result = []
    dy, dx = dir[bang]
    ny, nx = y, x
    while True:
        ny, nx = ny + dy, nx + dx
        # 1. 범위 벗어난 경우
        if nx < 0 or ny < 0 or nx >= N or ny >= N: return []

        # 2. 돌이 없는 경우(빈칸인 경우)
        if board[ny][nx] == 0: return []

        # 3. 같은색 돌을 발견
        if board[ny][nx] == color: break

        # 다른색 돌 좌표 추가
        result.append((ny, nx))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    # 보드에 초기 돌 4개 세팅
    mid = N//2
    board[mid-1][mid-1] = W
    board[mid-1][mid] = B
    board[mid][mid-1] = B
    board[mid][mid] = W

    for _ in range(M):
        x, y, color = map(int, input().split())
        y, x = y - 1, x - 1

        # 돌을 둔다
        board[y][x] = color
        # 방향 탐색
        for bang in range(8):
            # 뒤집을 돌들의 좌표 배열을 얻는다.
            target_stones = get_reverse_stone(y, x, bang, color)

            # 뒤집을 돌이 있다면 돌을 뒤집는다.
            if target_stones:
                for ry, rx in target_stones:
                    if color == B: board[ry][rx] = B
                    else: board[ry][rx] = W

    b_cnt = 0
    w_cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == B : b_cnt += 1
            if board[r][c] == W : w_cnt += 1

    print(f'#{tc} {b_cnt, w_cnt}')