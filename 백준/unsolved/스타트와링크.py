# 스타트와 링크
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N

def start_link(x, start=0, level = 0):
    visited[x] = 1

    if level == N // 2:
        

