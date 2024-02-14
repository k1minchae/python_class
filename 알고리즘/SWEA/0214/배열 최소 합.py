# def f():
#     if len(temp) == N:
#         result.append(sum(temp))
#         return
#
#     for i in range(N):
#         if not visited_y[i]:
#             visited_y[i] = True
#             for j in range(N):
#                 if not visited_x[j]:
#                     visited_x[j] = True
#                     temp.append(arr[i][j])
#                     f()
#                     temp.pop()
#                     visited_x[j] = False
#             visited_y[i] = False
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     temp = []
#     result = []
#     visited_x = [False] * N
#     visited_y = [False] * N
#     f()
#     print(f'#{tc} {min(result)}')
#
#



def f(i):
    # 모든 행을 방문한 경우
    if i == N:
        result.append(sum(temp))
        return

    # 열 탐색
    for j in range(N):
        if not visited_y[j]:
            visited_y[j] = True
            temp.append(arr[i][j])
            # 다음 행
            f(i + 1)
            # 초기화
            temp.pop()
            visited_y[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = []
    result = []
    visited_y = [False] * N
    f(0)
    print(f'#{tc} {min(result)}')
