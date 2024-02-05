T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [-1, 1, 0, 0]

    score_list = [] # 점수의 모든 경우의 수

    for i in range(N):
        for j in range(N):
            score = -arr[i][j]
            for d in range(4):
                nx = j + dx[d]
                ny = i + dy[d]
                if 0 <= nx < N and 0 <= ny < N: # 범위 안이면
                    score += arr[ny][nx] # 해당 점수 추가
                else: # 가장자리를 맞춘 경우
                    score = 0
                    break
            if score < 0: # 점수가 음수일 경우 0점
                score = 0
            elif score % 2 == 0: # 짝수일경우 점수 두배
                score = 2 * score
            score_list.append(score) # 점수 list에 추가

    score_list.sort()
    print(f'#{tc} {score_list[-1]}') # 최대값 점수 출력'

    # 강사님 코드
    # max_score = 0
    # for i in range(1, N-1):
    #     for j in range(1, N-1):
    #         score = arr[i][j+1] + arr[i+1][j] + arr[i][j-1] + arr[i-1][j] - arr[i][j]
    #         if score > 0:
    #             if score % 2 == 0:
    #                 score *= 2
    #