T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 학생수, M 문제수
    correct_arr = list(map(int, input().split()))  # 정답
    student_arr = [list(map(int, input().split())) for _ in range(N)]  # 학생 답안지
    score_list = [[0 for _ in range(M)] for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if student_arr[n][m] == correct_arr[m]:  # 정답을 맞추고
                # 이전문제의 정답을 맞췄다면
                if (m - 1 >= 0) and student_arr[n][m - 1] == correct_arr[m - 1]:
                    score_list[n][m] = score_list[n][m - 1] + 1
                else:
                    score_list[n][m] = 1
            else:
                score_list[n][n] = 0

    max_score = 0
    min_score = float('inf')
    for personal_score in score_list:
        if sum(personal_score) > max_score:
            max_score = sum(personal_score)
        if sum(personal_score) < min_score:
            min_score = sum(personal_score)
    print(f'#{tc} {max_score - min_score}')
