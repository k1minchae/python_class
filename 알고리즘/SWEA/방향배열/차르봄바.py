T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [1, -1, 0, 0]

    cnt_list = [] # 좌표별 모든 count 값을 넣은 리스트
    for i in range(N):
        for j in range(N):
            cnt = lst[i][j]     # 좌표 변할때마다 초기화하면서 현위치값도 더해줌
            for l in range(4):
                for k in range(1, M + 1):
                    ny = i + dy[l] * k
                    nx = j + dx[l] * k
                    if 0 <= ny < N and 0 <= nx < N: # 필드 벗어나지 않는 조건
                        cnt += lst[ny][nx]  # 폭탄 터지는 범위에 해당하는 값 더함
            cnt_list.append(cnt)    # 좌표 달라지기 전에 최종 count 값을 리스트에 넣음
    print(f'#{tc} {max(cnt_list)}') # 모든 좌표의 count 값중에 최대값 출력
