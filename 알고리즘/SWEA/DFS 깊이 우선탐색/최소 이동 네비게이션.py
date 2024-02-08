adjl = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [0, ],
    [5],
    [1],
    [1],
    []
]
A, B = map(int, input().split())
visited = [0] * 7
cnt = 0

def dfs(A):
    global cnt
    cnt += 1
    visited[A] = 1
    if A == B:
        if cnt < min_cnt:
            min_cnt = cnt
            return
    for w in adjl[A]:
        if visited[w] == 0:
            dfs(w)

dfs(A)
print(min_cnt)