# 전자카트
# def cart(s, cnt=1, val = 0):
#     global min_v
#     if cnt == N:
#         min_v = min(min_v, val+arr[s][0])
#         return
#     for j in range(N):
#         if not visited[j] and arr[s][j]:
#             visited[j] = 1
#             x = j
#             cart(x, cnt + 1, val+arr[s][x])
#             visited[j] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     min_v = float('inf')
#     visited = [0] * N
#     visited[0] = 1
#     cart(0)
#     print(f'#{tc} {min_v}')



# 강사님 코드
def dfs(cur, start, total):
    global result
    if cur == n - 1: # 가지치기
        result = min(result, arr[start][0] + total)
        return
    for i in range(1, n):
        if visited[i] == 0 and start != i:
            visited[i] = 1
            dfs(cur + 1, i, total + arr[start][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    result = float('inf')
    dfs(0, 0, 0)
    print(f'#{tc} {result}')
