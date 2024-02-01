N, M = map(int, input().split())  # 세로, 가로
K = int(input())  # 화력
arr = [list(input()) for _ in range(N)]


dx = [0, 0, -1, 1] # 상 하 좌 우
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '@': # 순회중에 폭탄을 만나면
            arr[i][j] = '%' # 일단 폭탄 자리는 터뜨림
            for d in range(4):  # x, y의 델타값을 위한 순회
                for k in range(1, 1+K):
                    ny = i + dy[d] * k # 폭탄 터지는 범위
                    nx = j + dx[d] * k
                    if 0 <= ny < N and 0 <= nx < M: # 인덱스 값을 벗어나지 않게 하는 조건
                        if arr[ny][nx] == '#': # 벽을 만나면
                            break
                        if arr[ny][nx] == '_': # 빈 칸을 만나면
                            arr[ny][nx] = '%'

for i in arr:
    print(*i, sep= '')