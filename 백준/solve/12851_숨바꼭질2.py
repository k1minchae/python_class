from collections import deque
N, K = map(int, input().split())
visited = [-1] * 100001
visited[N] = 0
result = 10 ** 6
cnt = 0
def BFS():
    global cnt, result
    q = deque([N])
    while q:
        x = q.popleft()
        if x == K:
            result = visited[x]
            cnt += 1
        if 2 * x < 100001 and (visited[2 * x] == -1 or visited[2 * x] >= visited[x] + 1):
            visited[2 * x] = visited[x] + 1
            q.append(2 * x)
        if 1 + x < 100001 and (visited[x + 1] == -1 or visited[x + 1] >= visited[x] + 1):
            q.append(x+1)
            visited[x+1] = visited[x] + 1
        if x - 1 >= 0 and (visited[x - 1] == -1 or visited[x - 1] >= visited[x] + 1):
            q.append(x-1)
            visited[x-1] = visited[x] + 1
BFS()
print(result)
print(cnt)