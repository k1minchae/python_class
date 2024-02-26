T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dy = [-2, -1, 2, 1, 0, 0, 0, 0] # 상하좌우
    dx = [0, 0, 0, 0, -1, -2, 1, 2]

    max_score = 0   # 보너스점수의 최댓값 초기화
    for i in range(N):
        for j in range(N):
            score = arr[i][j]
            for d in range(8):
                ny = dy[d] + i
                nx = dx[d] + j
                if 0 <= ny < N and 0 <= nx < N:
                    score += arr[ny][nx]
            if score > max_score:
                max_score = score
    print(f'#{tc} {max_score}')