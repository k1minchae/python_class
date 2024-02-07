T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]  # 상 하 좌 우
    dy = [1, -1, 0, 0]

    cnt_list = []
    for i in range(N):
        for j in range(N):
            cnt = lst[i][j]
            for l in range(4):
                for k in range(1, M + 1):
                    ny = i + dy[l] * k
                    nx = j + dx[l] * k
                    if 0 <= ny < N and 0 <= nx < N:
                        cnt += lst[ny][nx]
            cnt_list.append(cnt)
    print(f'#{tc} {max(cnt_list)}')