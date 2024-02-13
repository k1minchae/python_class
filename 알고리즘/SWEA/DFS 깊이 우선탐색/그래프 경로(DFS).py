# 2024 02 13 화요일

def btrack(S, G, visited):
    visited.append(S)
    if S == G:
        global result
        result = 1
        return
    else:
        for i in arr[S]:
            if i not in visited:
                btrack(i, G, visited)


T = int(input())
for tc in range(1, T+1):
    result = 0
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visited = []
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start].append(end)
    S, G = map(int, input().split()) # 출발, 도착 노드
    btrack(S,G, visited)
    print(f'#{tc} {result}')