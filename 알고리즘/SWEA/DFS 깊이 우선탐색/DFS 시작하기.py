def dfs(i):
    result.append(i)
    visited[i] = 1

    for w, j in enumerate(adjl[i]):
        if j == 1 and visited[w] == 0:
            dfs(w)

n = int(input())
adjl = [list(map(int, input().split())) for _ in range(n)]

result = []
visited = [0] * (n)
dfs(0)
print(*result)

# 강사님 코드
# def dfs(now): # now: 현재 노드에서 다른 노드 i 로의 경로가 있는지 탐색
#     print(now, end= ' ')
#     for i in range(n):
#         if MAP[now][i] == 0: # 경로가 없으면?
#             continue # 탐색 X
#         dfs(i) # 경로가 있을 때만 탐색
# n = int(input())
# MAP = [[int(x) for x in input().split()] for _ in range(n)]
# dfs(0)