def dfs(i, n): # i~end
    visited = [0] * (n)
    stack = []
    visited[i] = 1 # 시작점 방문
    result.append(i)

    while True:
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                result.append(i)
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return

n = int(input())  # 노드의 수
adjl = [list(map(int, input().split())) for _ in range(n)]  # 인접행렬
for i in range(n):
    for j in range(n):
        if adjl[i][j] == 1:
            adjl[i][j] = j
result = []
dfs(0, n)
print(*result)

# 강사님 코드
# 현재 노드에서 다른 노드로의 경로가 있을 때만 경로를 따라 탐색
# def dfs(now):
#     print(now, end = ' ')
#     for i in range(n):
#         if MAP[now][i] == 1:
#             dfs(i)
# n = int(input())
# MAP = [list(map(int, input().split())) for _ in range(n)]
# dfs(0)
