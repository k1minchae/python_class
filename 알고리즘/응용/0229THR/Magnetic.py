# Magnetic
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1 : 빨강, 2: 파랑

    is_red = False
    b_cnt = 0
    for j in range(N):  # 열 검사
        for i in range(N):
            if arr[i][j] == 1:  # 빨강
                is_red = True
            elif arr[i][j] == 2 and is_red:
                b_cnt += 1
                is_red = False
        is_red = False

    print(f'#{tc} {b_cnt}')

# 강사님 코드
# 열 검사 함수
# def v_cnt(col):
#     cnt = 0
#     # red 자성체를 체크
#     is_red = False
#
#     for row in range(N):
#         # red발견
#         if arr[row][col] == 1:
#             is_red = True
#         # 이전에 red발견하고 현재 blue라면
#         if arr[row][col] == 2 and is_red:
#             cnt += 1
#             is_red = False
#     return cnt
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     total_cnt = 0
#     # 열 순회하면서 토탈카운트 누적
#     for col in range(N):
#         total_cnt += v_cnt(col)
#     print(f'#{tc} {total_cnt}')