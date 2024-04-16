# 문제집
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
cnt_lst = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
    cnt_lst[b-1] += 1

q = []
visited = [0] * N
result = []
for i in range(N):
    if not cnt_lst[i]:
        heappush(q, i)
        visited[i] = 1
while q:
    x = heappop(q)
    result.append(x+1)
    for nx in adj[x]:
        if not visited[nx]:
            cnt_lst[nx] -= 1
            if not cnt_lst[nx]:
                visited[nx] = 1
                heappush(q, nx)

print(*result)