# 그룹나누기
from collections import deque

# 인접 리스트를 (그룹을) 전부 탐색하는 BFS
def BFS(start):
    q = deque([start])
    visited[start] = 1
    while q:
        node = q.popleft()
        if adj[node]:
            for next in adj[node]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = 1

# 입력받음
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접리스트 만들기
    adj = [[] for _ in range(N+1)]
    for i in range(0, 2 * M - 1, 2):
        adj[arr[i]].append(arr[i+1])
        adj[arr[i+1]].append(arr[i])

    # 결과 출력
    result = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if not visited[i]: # 어디도 속해있지 않는다면 새로운 그룹 추가해야함
            result += 1 # 그룹의 수
            BFS(i)

    print(f'#{tc} {result}')