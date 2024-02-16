from collections import deque
def BFS():
    visited = [0] * V
    q = deque()
    visited[S-1] = 1
    q.append(S-1)

    while q:
        v = q.popleft()
        if v == G-1:
            return visited[v] - 1
        for w in arr[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

# 입력
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)
    S, G = map(int, input().split())

    # 함수 호출
    result = BFS()
    print(f'#{tc} {result}')