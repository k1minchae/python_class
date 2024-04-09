# ACM Craft
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def bfs(target):
    q = deque([target])
    visited = [0] * (N + 1)
    visited[target] = 1
    t = time[target]
    while q:
        x = q.popleft()
        max_t = 0
        for n in arr[x]:
            if not visited[n]:
                max_t = max(time[n], max_t)
                visited[n] = 1
                q.append(n)
        t += max_t
    return t
for _ in range(T):
    N, K = map(int, input().split()) # 노드, 간선
    arr = [[] for _ in range(N + 1)]
    time = [0] + list(map(int, input().split())) # 건설에 걸리는 시간
    for _ in range(K):
        X, Y = map(int, input().split()) # 건설 순서 (Y를 지으려면 X가 필요)
        arr[Y].append(X)
    W = int(input()) # 건설해야할 건물 번호



    print(bfs(W))