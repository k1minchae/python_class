# Contact
from collections import deque
def BFS(start, tc):
    q = deque([start])
    visited[start] = 1

    while q:
        node = q.popleft()
        for next in adj[node]:
            if not visited[next]:
                visited[next] = visited[node] + 1
                q.append(next)
    max_v = max(visited)
    for i in range(100, 0, -1):
        if visited[i] == max_v:
            print(f'#{tc} {i}')
            return

for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    for i in range(0, N, 2):
        adj[arr[i]].append(arr[i+1])
    visited = [0] * 101
    BFS(S, tc)

