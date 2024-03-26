# 최소비용 구하기 2
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
adj = [[]for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
S, E = map(int, input().split())
result = [[float('inf'), []] for _ in range(N+1)]
pq = [(0, S, [S])]
while pq:
    c, n, temp = heappop(pq)
    if c > result[n][0]:
        continue
    for nc, nn in adj[n]:
        new_c = nc + c
        if new_c >= result[nn][0]:
            continue
        result[nn][0] = new_c
        result[nn][1] = temp + [nn]
        heappush(pq, (new_c, nn, temp+[nn]))
print(result[E][0])
print(len(result[E][1]))
print(*result[E][1])