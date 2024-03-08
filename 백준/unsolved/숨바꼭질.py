# 13549 숨바꼭질
from collections import deque
N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
temp = [N]
def BFS():
    q = deque([N])
    while q:
        x = q.popleft()
        if x == K:
            return visited[K] - 1, temp
        if 2 * x < 100001 and not visited[2*x]:
            q.append(2*x)
            visited[2*x] = visited[x]
            temp.append(2*x)
        if x-1 >= 0 and not visited[x-1]:
            q.append(x-1)
            visited[x-1] = visited[x] + 1
            temp.append(x-1)
        if x + 1 < 100001 and not visited[x+1]:
            q.append(x+1)
            visited[x+1] = visited[x] + 1
            temp.append(x+1)
print(BFS())
