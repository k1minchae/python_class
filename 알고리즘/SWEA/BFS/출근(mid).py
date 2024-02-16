# 출근(mid)
from collections import deque
def BFS():
    visited = [0] * N
    q = deque()
    q.append(0)
    visited[0] = 1

    while q:
        v = q.popleft()

        if v == N-1:
            return visited[v] -1

        for w in arr[v]:
            if visited[w] == 0 and w != T-1:
                q.append(w)
                visited[w] = visited[v] + 1
    return -1


# 입력 받는 곳
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
T = int(input())
result = BFS()
print(result)