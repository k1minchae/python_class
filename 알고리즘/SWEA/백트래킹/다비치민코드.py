# 다비치 민코드
# from itertools import combinations
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# M_arr = list(combinations(arr, M))
# min_v = float('inf')
# result = ()
# for i in M_arr:
#     cal = 1
#     for j in i:
#         cal *= j
#     if cal < min_v:
#         min_v = cal
#         result = i
# result = sorted(result)
# print(*result)
def backtracking(cnt, cal, last_index):
    global min_cal, min_result
    if cnt == M:
        if cal < min_cal:
            min_cal = cal
            min_result = result.copy()  # 최소값 업데이트
        return

    for i in range(last_index, N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])

            backtracking(cnt + 1, cal * arr[i], i + 1)

            visited[i] = False
            result.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
result = []
min_cal = float('inf')
min_result = []
backtracking(0, 1, 0)

print(*min_result)