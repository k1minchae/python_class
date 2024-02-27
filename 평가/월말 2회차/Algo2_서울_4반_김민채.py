# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_score = 0
#     visited_X = [0] * N
#     def balloon(i, score = 0, cnt = 0):
#         global max_score
#         if i == N:
#             if cnt == 3: # 3칸을 다 골랐을 때만 카운트
#                 max_score = max(score, max_score)
#             return
#         for j in range(N):
#             if visited_X[j] == 0 and arr[i][j] > 0:
#                 visited_X[j] = 1
#                 balloon(i + 1, score + arr[i][j], cnt + 1)
#                 visited_X[j] = 0    # 백트래킹
#         return
#
#     balloon(0)
#     print(f'#{tc}', max_score)

def func(i, k, s):
    global max_v
    if i == k:
        if max_v < s:
            max_v = s
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            if target[i][p[i]] > 0:  # 실격이 되는 표적 제외
                func(i + 1, k, s + target[i][p[i]])
            p[i], p[j] = p[j], p[i]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    target = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    max_v = 0
    func(0, N, 0)
    print(f'#{tc} {max_v}')