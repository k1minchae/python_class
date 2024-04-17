# 별자리 만들기
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M, tar = map(int, input().split())
tar -= 1
adj = [[]for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a-1].append((c, b-1))
    adj[b-1].append((c, a-1))
visited = [[float('inf'), ''] for _ in range(N)]
visited[0][0] = 0
visited[0][1] = '0'
q = [(0, '0')]
while q:
    cost, path = heappop(q)
    node = int(path[-1])
    if cost > visited[node][0]:
        continue
    for c, next_node in adj[node]:
        next_cost = cost + c
        if visited[next_node][0] < next_cost:
            continue
        next_path = path + str(next_node)
        heappush(q, (next_cost, next_path))
        visited[next_node][0] = next_cost
        if visited[next_node][0] == next_cost:
            visited[next_node].append(next_path)
        else:
            visited[next_node].clear()
            visited[next_node].append(next_cost, next_path)
print(visited)
for i in range(1, len(visited[N-1])):
    if str(tar) in visited[N-1][i]:
        print('SAVE HIM')
        break
else:
    print('GOOD BYE')