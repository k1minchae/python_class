# 인접행렬 BFS 시작(low)
from collections import deque
def BFS(start):  # 시작점
    q.append(start)
    visited.append(start)
    while q: # q 가 남아있으면
        s = q.popleft()
        for node, link in enumerate(arr[s]):
            if link == 1 and node not in visited:   # 연결 O
                q.append(node)
                visited.append(node)
    return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
visited = []
BFS(0)
print(*visited)