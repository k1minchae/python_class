# 여행 가자
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split())) + [0]
plan = deque(plan)
if N == 1:
    print('YES')
else:
    def BFS(start):
        q = deque([start])
        # visited = [0] * N
        # visited[start] = 1
        city = plan.popleft()
        while q:
            node = q.popleft()
            if node + 1 == city:
                city = plan.popleft()
                if city == 0:
                    return 'YES'
            for n in range(N):
                if arr[node][n]:
                    q.append(n)
                    # visited[n] = 1
        return 'NO'

    print(BFS(plan[0] - 1))