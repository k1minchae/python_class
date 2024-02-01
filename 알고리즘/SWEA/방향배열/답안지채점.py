T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 학생수, M 문제수
    correct_arr = list(map(int, input().split())) # 정답지
    student_arr = [list(map(int, input().split())) for _ in range(N)] # 학생 답안지
    score_list = [[0 for _ in range(M)] for _ in range(N)] # 각 학생별, 문제별 점수list

    for n in range(N):
        for m in range(M):
            # 정답을 맞추고
            if student_arr[n][m] == correct_arr[m]:
                 # 이전문제의 정답까지 맞췄다면
                if (m-1 >= 0) and student_arr[n][m-1] == correct_arr[m-1]:
                    # 현재 점수 = 이전 문제의 점수 + 1
                    score_list[n][m] = score_list[n][m-1] + 1
                else: # 이전문제는 틀리고, 현재 문제만 맞췄다면
                    score_list[n][m] = 1 # 현재 점수 = 1
            else: # 문제를 그냥 틀렸다면
                score_list[n][n] = 0

    max_score = float('-inf') # 어차피 scorelist를 순회해서 업데이트 할거라서 임의의 작은수 넣어둠
    min_score = float('inf')  # 이건 임의로 큰 수 넣어둠
    for personal_score in score_list:
        if sum(personal_score) > max_score: # 최대값 업데이트
            max_score = sum(personal_score)
        if sum(personal_score) < min_score: # 최소값 업데이트
            min_score = sum(personal_score)
    print(f'#{tc} {max_score - min_score}')
