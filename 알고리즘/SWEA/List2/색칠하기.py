T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0 # 보라색 카운트
    for _ in range(N):
        x_s, y_s, x_e, y_e, c = map(int, input().split())
        # x시작, y시작, x끝, y끝, 색깔

        for j in range(x_s, x_e+1):
            for i in range(y_s, y_e+1):
                if arr[i][j] == 0: # 아무색도 안칠해져있으면
                    arr[i][j] = c # 색깔로 칠해버리기
                    
                else: # 이미 다른색이 칠해져있으면
                    cnt += 1 # 보라색 카운트
    print(f'#{tc} {cnt}')