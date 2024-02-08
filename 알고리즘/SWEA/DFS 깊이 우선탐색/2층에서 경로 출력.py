def dfs(i, ans = '0', level = 0):
    level += 1
    visited[i] = 1
    ans += ' ' + str(i)
    if level == 2:
        print(ans)
        return
    for w, j in enumerate(adjl[i]):
        if j == 1 and visited[w] == 0:
            dfs(w, ans, level)


n = int(input())
adjl = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
visited[0] = 1
for idx, j in enumerate(adjl[0]):
    if j == 1:
        dfs(idx)


# 강사님 코드
n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
# path 는 현재 탐색중인 경로를 기록
path = [0] * 10

def dfs(level, now):
    if level == 2: # 출력
        for i in range(level + 1):
            print(path[i], end = " ")
        print()
        return
    for i in range(n):
        if MAP[now][i] == 1: # 다음 경로가 존재하면
            path[level + 1] = i # 경로를 기록
            dfs(level + 1, i) # 다음 레벨로 dfs
            path[level + 1] = 0 # 탐색 끝나면 경로 초기화
dfs(0, 0)