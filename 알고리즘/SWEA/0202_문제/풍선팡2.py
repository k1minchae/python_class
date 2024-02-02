T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로: N   가로 :M
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    count_list = []

    # 각 위치에서의 꽃가루 터뜨리기 시뮬레이션
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]  # 처음 고른 위치 터뜨려서 꽃가루 카운트

            # 상하좌우로 퍼져나가면서 꽃가루 카운트
            for d in range(4):
                # 터지는 범위가 필드 밖으로 벗어나지 않도록 조건문 추가
                if (N > i + dy[d] >= 0) and (M > j + dx[d] >= 0):
                    cnt += arr[i + dy[d]][j + dx[d]]
            count_list.append(cnt)  # 각 위치별 꽃가루 터지는 개수를 count_list 에 추가

            # 그 중에서 max값 출력
    print(f'#{tc} {max(count_list)}')

