# 수학 게임 페스티벌(high)
from collections import deque

def festival(s, res=''):
    visited = [0] * 10000
    q = deque()
    q.append([s, ''])
    while True:
        x, res = q.popleft()
        if x == B:
            return res
        if not visited[x * 2 % 10000]:
            q.append([x * 2 % 10000, res + 'D'])
            visited[x * 2 % 10000] = 1
        if not visited[x - 1]:
            q.append([x - 1, res + 'S'])
            visited[x - 1] = 1
        if not visited[(x % 1000 * 10 + x // 1000) % 10000]:
            visited[(x % 1000 * 10 + x // 1000) % 10000] = 1
            q.append([(x % 1000 * 10 + x // 1000) % 10000, res + 'L'])
        if not visited[(x % 10 * 1000 + x // 10) % 10000]:
            visited[(x % 10 * 1000 + x // 10) % 10000] = 1
            q.append([(x % 10 * 1000 + x // 10) % 10000, res + 'R'])

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print(festival(A))